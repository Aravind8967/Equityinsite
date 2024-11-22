from django.db import models

class nifty_50(models.Model):
    name = models.CharField(max_length = 50)
    symbol = models.CharField(max_length = 10)
    exchange = models.CharField(max_length = 10)
    sector = models.CharField(max_length = 30)
    industry = models.CharField(max_length = 30)
    market_cap = models.IntegerField()

class nifty_next(models.Model):
    name = models.CharField(max_length = 50)
    symbol = models.CharField(max_length = 10)
    exchange = models.CharField(max_length = 10)
    sector = models.CharField(max_length = 30)
    industry = models.CharField(max_length = 30)
    market_cap = models.IntegerField()

class nifty_midcap(models.Model):
    name = models.CharField(max_length = 50)
    symbol = models.CharField(max_length = 10)
    exchange = models.CharField(max_length = 10)
    sector = models.CharField(max_length = 30)
    industry = models.CharField(max_length = 30)
    market_cap = models.IntegerField()

class nifty_smallcap(models.Model):
    name = models.CharField(max_length = 50)
    symbol = models.CharField(max_length = 10)
    exchange = models.CharField(max_length = 10)
    sector = models.CharField(max_length = 30)
    industry = models.CharField(max_length = 30)
    market_cap = models.IntegerField()
    
class nifty_bank(models.Model):
    name = models.CharField(max_length = 50)
    symbol = models.CharField(max_length = 10)
    exchange = models.CharField(max_length = 10)
    sector = models.CharField(max_length = 30)
    industry = models.CharField(max_length = 30)
    market_cap = models.IntegerField()

class nifty_finance(models.Model):
    name = models.CharField(max_length = 50)
    symbol = models.CharField(max_length = 10)
    exchange = models.CharField(max_length = 10)
    sector = models.CharField(max_length = 30)
    industry = models.CharField(max_length = 30)
    market_cap = models.IntegerField()

class nifty_psu_bank(models.Model):
    name = models.CharField(max_length = 50)
    symbol = models.CharField(max_length = 10)
    exchange = models.CharField(max_length = 10)
    sector = models.CharField(max_length = 30)
    industry = models.CharField(max_length = 30)
    market_cap = models.IntegerField()

class nifty_it(models.Model):
    name = models.CharField(max_length = 50)
    symbol = models.CharField(max_length = 10)
    exchange = models.CharField(max_length = 10)
    sector = models.CharField(max_length = 30)
    industry = models.CharField(max_length = 30)
    market_cap = models.IntegerField()

class nifty_auto(models.Model):
    name = models.CharField(max_length = 50)
    symbol = models.CharField(max_length = 10)
    exchange = models.CharField(max_length = 10)
    sector = models.CharField(max_length = 30)
    industry = models.CharField(max_length = 30)
    market_cap = models.IntegerField()

class nifty_metal(models.Model):
    name = models.CharField(max_length = 50)
    symbol = models.CharField(max_length = 10)
    exchange = models.CharField(max_length = 10)
    sector = models.CharField(max_length = 30)
    industry = models.CharField(max_length = 30)
    market_cap = models.IntegerField()

class nifty_pharma(models.Model):
    name = models.CharField(max_length = 50)
    symbol = models.CharField(max_length = 10)
    exchange = models.CharField(max_length = 10)
    sector = models.CharField(max_length = 30)
    industry = models.CharField(max_length = 30)
    market_cap = models.IntegerField()
