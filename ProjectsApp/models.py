from django.db import models 

class Project(models.Model):
        name = models.CharField(max_length=100)
        begin = models.DateField()
        end = models.DateField(blank=True, null=True)
        active=models.BooleanField()
        #se dejan blank en true y null porque puede no tener fecha de fin aun. 
        #Se pueden agregar mas pero estos son los necesarios
        def __unicode__(self):
            return self.name
        #Para el ordenamiento se hace por el nombre debido a que es mas sencillo que buscar por fecha de inicio 
        #y la final no siempre esta definida
        class Meta:
            ordering = ['name']

class Task(models.Model):
	   #Las tareas van a ocupar tres campos elementales en la base de datos
        name = models.CharField(max_length=150)
        begin= models.DateField()
        end = models.DateField(blank=True, null=True)
        description = models.CharField(blank=True, null=True, max_length=400)
        active=models.BooleanField()
        project = models.ForeignKey(Project)

        #se dejan blank en true y null porque puede no tener fecha de fin aun. 
        #Se pueden agregar mas pero estos son los necesarios

        def __unicode__(self):
            return self.name

        class Meta:
            ordering = ['name']
