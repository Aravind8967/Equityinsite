from django.contrib import admin
from indexes.models import nifty_50,nifty_next, nifty_midcap, nifty_smallcap, nifty_bank, nifty_finance
from indexes.models import nifty_psu_bank, nifty_it, nifty_auto, nifty_metal, nifty_pharma

class nifty_50_admin(admin.ModelAdmin):
    list_display = ("name", "symbol", "exchange", "sector", 
                    "industry", "market_cap")

class nifty_next_admin(admin.ModelAdmin):
    list_display = ("name", "symbol", "exchange", "sector", 
                    "industry", "market_cap")

class nifty_midcap_admin(admin.ModelAdmin):
    list_display = ("name", "symbol", "exchange", "sector", 
                    "industry", "market_cap")

class nifty_smallcap_admin(admin.ModelAdmin):
    list_display = ("name", "symbol", "exchange", "sector", 
                    "industry", "market_cap")

class nifty_bank_admin(admin.ModelAdmin):
    list_display = ("name", "symbol", "exchange", "sector", 
                    "industry", "market_cap")

class nifty_finance_admin(admin.ModelAdmin):
    list_display = ("name", "symbol", "exchange", "sector", 
                    "industry", "market_cap")

class nifty_psu_bank_admin(admin.ModelAdmin):
    list_display = ("name", "symbol", "exchange", "sector", 
                    "industry", "market_cap")

class nifty_it_admin(admin.ModelAdmin):
    list_display = ("name", "symbol", "exchange", "sector", 
                    "industry", "market_cap")

class nifty_auto_admin(admin.ModelAdmin):
    list_display = ("name", "symbol", "exchange", "sector", 
                    "industry", "market_cap")

class nifty_metal_admin(admin.ModelAdmin):
    list_display = ("name", "symbol", "exchange", "sector", 
                    "industry", "market_cap")

class nifty_pharma_admin(admin.ModelAdmin):
    list_display = ("name", "symbol", "exchange", "sector", 
                    "industry", "market_cap")
    
admin.site.register(nifty_50, nifty_50_admin)
admin.site.register(nifty_next, nifty_next_admin)
admin.site.register(nifty_midcap, nifty_midcap_admin)
admin.site.register(nifty_smallcap, nifty_smallcap_admin)
admin.site.register(nifty_bank, nifty_bank_admin)
admin.site.register(nifty_finance, nifty_finance_admin)
admin.site.register(nifty_psu_bank, nifty_psu_bank_admin)
admin.site.register(nifty_it, nifty_it_admin)
admin.site.register(nifty_auto, nifty_auto_admin)
admin.site.register(nifty_metal, nifty_metal_admin)
admin.site.register(nifty_pharma, nifty_pharma_admin)