#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
    user = models.OneToOneField(User)
#    willbethere = models.BooleanField(verbose_name="Je serai présent à la PyconFr2015", default=False)
    willbepresentsaturday = models.BooleanField(verbose_name="Je serai présent Samedi", default=False)
    willbetheresunday = models.BooleanField(verbose_name="Je serai présent Dimanche", default=False)
    goodies = models.BooleanField(verbose_name="Goodie (offert)", default=True)
    tshirtsize = models.CharField(verbose_name="Je pré-reserve un T-shirt de taille",max_length=5, choices=(('', 'non merci'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')), null=True, default='', blank=True)
    diner = models.BooleanField(verbose_name="Je m'inscris au diner du Samedi soir", default=False)
    iarriveby = models.CharField(verbose_name="J'arrive", null=True, choices=(('', '---'),('en train', 'en train'), ('en voiture', 'en voiture'), ('en avion', 'en avion')), default='', max_length=55, blank=True)
    arrivaldate = models.CharField(verbose_name="Jour d'arrivée", null=True, choices=(('', '---'),('vendredi', 'vendredi'), ('samedi', 'samedi'), ('dimanche', 'dimanche')), default='', max_length=55, blank=True)
    arrivalhour = models.CharField(verbose_name="Heure d'arrivée", max_length=5, blank=True)
    iwillgoby = models.CharField(verbose_name="Je partirai", null=True, choices=(('', '---'), ('en train', 'en train'), ('en voiture', 'en voiture'), ('en avion', 'en avion')), default='', max_length=55, blank=True)
    dateofdeparture = models.CharField(verbose_name="Jour de départ", null=True, choices=(('','---'),('samedi', 'samedi'), ('dimanche', 'dimanche'), ('lundi', 'lundi'), ('mardi', 'mardi')), default='', max_length=55, blank=True)
    hourofdeparture = models.CharField(verbose_name="Heure de départ", max_length=5, blank=True)
    phone = models.CharField(verbose_name="Mon tel pour la logistique", max_length=10, blank=True)    

    @models.permalink
    def get_absolute_url(self):
        return ('poll_detail', [str(self.id)])
    
    def __unicode__(self):
        return self.user.username


    
