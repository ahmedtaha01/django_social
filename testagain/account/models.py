from django.db import models
from django.contrib.auth.models import AbstractUser
from urllib.request import urlopen
from django.core.files import File 
from django.core.files.temp import NamedTemporaryFile
from django.http import HttpResponse
import os
from urllib import request
# Create your models here.

class Auser(AbstractUser):
    ginder = models.CharField(max_length=10)
    picture = models.ImageField(upload_to='account/image',null=True)



    def get_image_from_url(self, url):
        # img_tmp = NamedTemporaryFile()
        # with urlopen(url) as uo:
        #     assert uo.status == 200
        #     img_tmp.write(uo.read())
        #     img_tmp.flush()
        # img = File(img_tmp)
        # self.picture.save(img_tmp.name, img)
        # ////////////////////
        # result = urllib.urlretrieve(self.image_url)
        # self.image_file.save(
        #         os.path.basename(self.image_url),
        #         File(open(result[0]))
        #         )
        # self.save()
        # //////////////////////////////
        # result = request.urlretrieve(url)
        # self.picture.save(
        #         os.path.basename(url+'.jbg'),
        #         File(open(result[0], 'rb'))
        #         )
        # //////////////////////////////////
        img_temp = NamedTemporaryFile()
        img_temp.write(urlopen(url).read())
        img_temp.flush()
        self.picture.save("image_%s" % self.pk +'.jpg', File(img_temp))
        self.save()
               
