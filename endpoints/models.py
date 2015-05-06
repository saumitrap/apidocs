from django.db import models

class Group(models.Model):
	label = models.CharField(max_length=255)
	descr = models.TextField()
	order_rank = models.PositiveSmallIntegerField(default=99)

	class Meta:
		ordering = ['order_rank', '-id']

	def __unicode__(self):
		return '%s' % self.label


class Endpoint(models.Model):
	GET = 1
	POST = 2
	PUT = 3
	DELETE = 4
	METHOD_CHOICES = (
		(GET, 'GET'),
		(POST, 'POST'),
		(PUT, 'PUT'),
		(DELETE, 'DELETE'),
	)

	group = models.ForeignKey(Group)
	label = models.CharField(max_length=255)
	method = models.PositiveSmallIntegerField(choices=METHOD_CHOICES)
	url = models.CharField(max_length=255)
	descr = models.TextField(help_text="Supports Markdown")
	request_example = models.TextField()
	response_example = models.TextField()
	response_descr = models.TextField()
	order_rank = models.PositiveSmallIntegerField(default=99)

	def __unicode__(self):
		return '%s %s' % (self.get_method_display(), self.url)


class Param(models.Model):
	PATH = 1
	REQUEST = 2
	PARAM_TYPE_CHOICES = (
		(PATH, 'Path Parameter'),
		(REQUEST, 'Request Parameter')
	)

	INTEGER = 1
	NUMBER = 2
	STRING = 3
	BOOLEAN = 4
	STRING_LIST = 5
	DATA_TYPE_CHOICES = (
		(INTEGER, 'integer'),
		(NUMBER, 'number'),
		(STRING, 'string'),		
		(BOOLEAN, 'boolean'),
		(STRING_LIST, 'string[]')
	)

	endpoint = models.ForeignKey(Endpoint)
	param_type = models.PositiveSmallIntegerField(choices=PARAM_TYPE_CHOICES)
	key = models.CharField(max_length=255)
	is_required = models.BooleanField(default=True)
	data_type = models.PositiveSmallIntegerField(choices=DATA_TYPE_CHOICES)
	descr = models.TextField(blank=True)
	order_rank = models.PositiveSmallIntegerField(default=99)


class Error(models.Model):
	endpoint = models.ForeignKey(Endpoint)
	code = models.PositiveSmallIntegerField(unique=True)
	message = models.CharField(max_length=1000)
	descr = models.TextField(blank=True)
	order_rank = models.PositiveSmallIntegerField(default=99)

