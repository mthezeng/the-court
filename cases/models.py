from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Case(models.Model):
	caption = models.CharField(max_length=200)
	argued_date = models.DateField()
	decided_date = models.DateField()
	citation = models.CharField(max_length=50)
	summary = models.TextField()
	commentary = models.TextField(blank=True)
	opinion_link = models.URLField(blank=True)
	case_opinions = models.ManyToManyField('Opinion', related_name='case')

	def __str__(self):
		return self.caption


class Opinion(models.Model):

	class OpinionType(models.TextChoices):
		MAJORITY = 'M', _('Majority')
		PLURALITY = 'P', _('Plurality')
		CONCURRING = 'C', _('Concurring')
		DISSENTING = 'D', _('Dissenting')
		CONCURRING_DISSENTING = 'CD', _('Concurring in part and dissenting in part')

	opinion_type = models.CharField(max_length=2, choices=OpinionType.choices, default=OpinionType.MAJORITY)
	author = models.ForeignKey('Justice', blank=True, on_delete=models.PROTECT, related_name='+')
	joined_by = models.ManyToManyField('Justice', blank=True, related_name='+')
	text_link = models.URLField(blank=True)

	def __str__(self):
		try:
			return '{0} opinion of {1} in {2}'.format(self.opinion_type, self.author, self.case.get(pk=1).caption)
		except Case.DoesNotExist:
			return '{0} opinion of {1}'.format(self.opinion_type, self.author)


class Justice(models.Model):
	first_name = models.CharField(max_length=20)
	middle_initial = models.CharField(max_length=1, null=True, blank=True)
	last_name = models.CharField(max_length=20)
	suffix = models.CharField(max_length=5, null=True, blank=True)
	is_chief_justice = models.BooleanField(default=False)
	is_sitting_justice = models.BooleanField(default=False)

	def __str__(self):
		if self.is_chief_justice:
			return 'Chief Justice {0} {1}'.format(self.first_name, self.last_name)
		else:
			return 'Justice {0} {1}'.format(self.first_name, self.last_name)


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	description = models.CharField(max_length=100, default='')
	city = models.CharField(max_length=100, default='')
	website = models.URLField(default='')
	phone = models.IntegerField(default=0)

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
