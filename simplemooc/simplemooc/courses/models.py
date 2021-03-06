from django.db import models
from django.conf import settings

from simplemooc.core.mail import send_mail_template

# Create your models here.
class CourseManager(models.Model):

	def search(self, query):
		return self.getquery().filter(
			models.Q(name__icontains=query) | \
			models.Q(description__icontains=query)
		)

class Course(models.Model):
	
	name = models.CharField(
		'Nome', 
		max_length=100 #max_length tamanho de caracteres do campo
	) 

	slug = models.SlugField(
		'Atalho'
	)

	description = models.TextField(
		'Descrição', 
		blank=True # blank = true -> quer dizer que o campo não é obrigatório
	) 

	about = models.TextField(
		'Sobre',
		blank=True
	)

	start_date = models.DateField(
		'Data de Início', 
		null=True, #null que no banco ele pode ser nulo
		blank=True 
	)

	image = models.ImageField(
		upload_to='courses/images', #pasta que serão salvos as imagens
		verbose_name='Imagem',
		null=True,
		blank=True
	)

	created_at = models.DateTimeField(
		'Criado em',
		auto_now_add=True #auto_now_add -> significa que somente quando for criado pegará a data atual
	) 

	updated_at = models.DateTimeField(
		'Atualizado em',
		auto_now=True #auto_now -> toda vez que for atualizado pegara a data atual
	) 

	objects = CourseManager();

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Curso'
		verbose_name_plural = 'Cursos'
		ordering = ['name']

class Enrollment(models.Model):

	STATUS_CHOICES = (
		(0, 'Pendente'),
		(1, 'Aprovado'),
		(2, 'Cancelado'),
	)

	user = models.ForeignKey(
		settings.AUTH_USER_MODEL, verbose_name='Usuario',
		on_delete=models.CASCADE,
		related_name='enrollments'
	)
	
	course = models.ForeignKey(
		Course, verbose_name='Curso',
		on_delete=models.CASCADE,
		related_name='enrollments'
	)

	status = models.IntegerField(
		'Situação', choices=STATUS_CHOICES, default=1, blank=True
	)

	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)

	def active(self):
		self.status = 1
		self.save()

	def is_approved(self):
		return self.status == 1	

	class Meta:
		verbose_name = 'Inscrição'
		verbose_name_plural = 'Inscrições'
		unique_together = (('user', 'course'))


class Announcement(models.Model):

	course = models.ForeignKey(Course, verbose_name = 'Curso', on_delete=models.CASCADE, related_name='announcements')
	title = models.CharField('Titulo', max_length=100)
	content = models.TextField('Conteudo')

	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Anúncio'
		verbose_name_plural = 'Anúncios'
		ordering = ['-created_at']


class Comment(models.Model):

	announcement = models.ForeignKey(
		Announcement, 
		verbose_name='Anúncio', 
		on_delete=models.CASCADE,
		related_name='comments'
	)

	user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='usuário', on_delete=models.CASCADE)
	comment = models.TextField('Comentário')

	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)

	class Meta:
		verbose_name = 'Comentário'
		verbose_name_plural = 'Comentários'
		ordering = ['created_at']

def post_save_announcement(instance, created, **kwargs):
	if created:
		subject = instance.title
		context = {
			'announcement': instance
		}
		template_name = 'courses/announcements_mail.html'
		enrollments = Enrollment.objects.filter(
			course=instance.course, status=1
		)
		for enrollment in enrollments:
			recipient_list = [enrollment.user.email]
			send_mail_template(subject, template_name, context, recipient_list)

models.signals.post_save.connect(
	post_save_announcement, sender=Announcement,
	dispatch_uid=''
)
