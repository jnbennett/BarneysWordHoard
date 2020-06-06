from django.db import models

class Word(models.Model):
	word = models.CharField(max_length=25, blank=True)
	definition_1 = models.CharField(max_length=250, blank=True)
	definition_2 = models.CharField(max_length=250, blank=True)
	definition_3 = models.CharField(max_length=250, blank=True)
	definition_4 = models.CharField(max_length=250, blank=True)
	definition_5 = models.CharField(max_length=250, blank=True)
	alternate_spellings = models.CharField(max_length=50, blank=True)
	CASE_CHOICES = (
			('', ''),
			('nom.', 'nominative'),
			('acc.', 'accusative'),
			('gen.', 'genitive'),
			('dat.', 'dative')
		)
	case = models.CharField(max_length=5, choices = CASE_CHOICES, default='', blank=True) 
	GENDER_CHOICES = (
			('', ''),
			('m.', 'masculine'),
			('f.', 'feminine'),
			('n.', 'neuter')
		)
	gender = models.CharField(max_length=2, choices = GENDER_CHOICES, default='', blank=True)

	class Meta:
		ordering = ['word']

	def __str__(self):
		return self.word

class Group(models.Model):
	group = models.CharField(max_length=3, blank =True)
	word = models.ForeignKey(Word, on_delete=models.CASCADE)
	history = models.CharField(max_length=2000, blank=True)
	frequency = models.CharField(max_length=3, blank=True)
	compounds = models.CharField(max_length=500, blank=True)

	class Meta:
		ordering = ['group']

	def __str__(self):
		return self.group
