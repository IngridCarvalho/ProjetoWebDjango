from django.db import models

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

