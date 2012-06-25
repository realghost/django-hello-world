from django.db import models

# Create your models here.
class RequestInfo(models.Model):
    """
    Model to save requests in DB. Stores ip, datetime, protocol, method, path,
    response status, response length, referrer, user agent
    """
    #CharField is used for ip because a list of proxy ip may be obtained
    ip = models.CharField(max_length=127)
    datetime = models.DateTimeField(auto_now_add=True)
    protocol = models.CharField(max_length=15)
    method = models.CharField(max_length=15)
    path = models.CharField(max_length=255)
    referer = models.CharField(max_length=255)
    response_status = models.IntegerField()
    response_tell = models.IntegerField()
    user_agent = models.CharField(max_length=255)
    
    def __unicode__(self):
        return "Requst from %s on %s" %(self.ip, 
                   self.datetime.strftime('%d.%m.%Y, %H:%M:%S'))
                   
    class Meta:
        ordering = ['-datetime']
        get_latest_by = 'datetime'
