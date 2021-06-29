# Deploymodel URL Configuration

from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
# from .views import SearchClass
# from .views import AboutView
# from .views import MyAboutView
urlpatterns = [
    path('',views.home,name='home'),
    path('search',views.search, name='search'),
    path('searched_filter',views.searched_filter, name='searched_filter'),
    path('fashion',views.fashion, name = 'fashion'),
    path('laptop',views.laptop, name='laptop'),

    
    path('camera',views.camera, name='camera'), 
    
  
    
    path('electronics',views.electronics, name='electronics'),
    path('mobile',views.mobile, name='mobile'),
    path('wears', views.wears, name = 'wears'),
    path('shoes',views.shoes, name = 'shoes'),
    path('wears_shoes', views.wears_shoes, name='wears_shoes'),
    path('beauty_health',views.beauty_health, name ='beauty_health'),
    path("products/<int:myid>", views.productview, name="Productview"),
    path("products_laptop/<int:myid>", views.productviewLaptop, name="productviewLaptop"),
    path('products_mobile/<int:myid>',views.productViewMobile, name = 'productViewMobile'),
    path('ascending_products_home',views.ascending_products_home, name='ascending_products_home'),
    path('descending_products_home',views.descending_products_home, name='descending_products_home'),
    path('ascending_products_electronics',views.ascending_products_electronics, name='ascending_products_electronics'),
    path('descending_products_electronics', views.descending_products_electronics, name='descending_products_electronics'),
    path('ascending_products_wears', views.ascending_products_wears, name= 'ascending_products_wears'),
    path('descending_products_wears', views.descending_products_wears, name= 'descending_products_wears'),
    path('ascending_products_search', views.ascending_products_search, name ='ascending_products_search'), 
    path('ascending_prod_mobile', views.ascending_prod_mobile, name= 'ascending_prod_mobile'),
    path('descending_prod_mobile', views.descending_prod_mobile, name='descending_prod_mobile'),
    path('ascending_prod_laptop', views.ascending_prod_laptop, name='ascending_prod_laptop'),
    path('descending_prod_laptop', views.descending_prod_laptop, name='descending_prod_laptop'),
    path('descending_prod_tv', views.descending_prod_tv, name='descending_prod_tv'),
    path('ascending_prod_tv', views.ascending_prod_tv, name='ascending_prod_tv'),
    path('ascending_prod_tablet',views.ascending_prod_tablet, name='ascending_prod_tablet'),
    path('descending_prod_tablet', views.descending_prod_tablet, name='descending_prod_tablet'),
    path('descending_prod_smart_watches', views.descending_prod_smart_watches , name='descending_prod_smart_watches'),
    path('ascending_prod_smart_watches', views.ascending_prod_smart_watches , name='ascending_prod_smart_watches'),
    # path('search', SearchClass.as_view(template_name="search.html")),
    # path('mobileTable/<str:product_name>',views.mobileTable, name = 'mobileTable'),
    path('wears_men', views.wears_men, name='wears_men'),
    path('wears_women',views.wears_women, name='wears_women'),
    # path('about_view', AboutView.as_view()),
    # path('shoes',MyAboutView.as_view()),
    path('slide', views.slide, name='slide.html'),
    path('home', views.home_prod, name = 'home.html'),
    path('appliances',views.appliances , name ='appliances'),
    path('pantry',views.pantry, name='pantry.html'),
    # path('laptop_brand',views.laptop_brand, name = 'laptop_brand'),

    # laptop-Brand-filter--
    path('laptop_brand_hp',views.laptop_brand_hp , name = 'laptop_brand_dell'),
    path('laptop_brand_dell',views.laptop_brand_dell , name = 'laptop_brand_dell'),
    path('laptop_brand_asus',views.laptop_brand_asus , name = 'laptop_brand_asus'),
    path('laptop_brand_lenovo',views.laptop_brand_lenovo , name = 'laptop_brand_lenovo'),
    path('laptop_brand_samsung',views.laptop_brand_samsung , name = 'laptop_brand_samsung'),
    path('laptop_brand_lg',views.laptop_brand_lg , name = 'laptop_brand_lg'),
    path('laptop_brand_acer',views.laptop_brand_acer , name = 'laptop_brand_acer'),
    path('laptop_brand_redmi',views.laptop_brand_redmi , name = 'laptop_brand_redmi'),

    # Mobile-Brand-filter--
    path('mobile_brand_redmi',views.mobile_brand_redmi , name = 'mobile_brand_redmi'),
    path('mobile_brand_samsung',views.mobile_brand_samsung , name = 'mobile_brand_samsung'),
    path('mobile_brand_realme',views.mobile_brand_realme , name = 'mobile_brand_realme'),
    path('mobile_brand_vivo',views.mobile_brand_vivo , name = 'mobile_brand_vivo'),
    path('mobile_brand_oppo',views.mobile_brand_oppo , name = 'mobile_brand_oppo'),
    path('mobile_brand_poco',views.mobile_brand_poco , name = 'mobile_brand_poco'),
    path('mobile_brand_apple',views.mobile_brand_apple , name = 'mobile_brand_apple'),
    path('mobile_brand_nokia',views.mobile_brand_nokia , name = 'mobile_brand_nokia'),
    path('mobile_brand_oneplus',views.mobile_brand_oneplus , name = 'mobile_brand_oneplus'),
    path('mobile_brand_infinix',views.mobile_brand_infinix , name = 'mobile_brand_infinix'),
    path('mobile_brand_asus',views.mobile_brand_asus , name = 'mobile_brand_asus'),
    path('mobile_brand_techno',views.mobile_brand_techno , name = 'mobile_brand_techno'),
    path('mobile_brand_huawei',views.mobile_brand_huawei, name='mobile_brand_huawei'),
    
    # Top-searched-electronics
    path('smartwatch',views.smartwatch, name='smartwatch'),
    path('headphone', views.headphone, name='headphone'),
    path('camera', views.camera, name='camera'),
    
    path('printer',views.printer, name='printer'),
    path('router',views.router, name='router'),
    path('home_theatre',views.home_theatre,name='home_theatre'),
    path('computer_accessories',views.computer_accessories,name='computer_accessories'),
    #Other electronics-products
    path('tablet_accessories',views.tablet_accessories, name='tablet_accessories'),
    path('gaming_accessories',views.gaming_accessories, name='gaming_accessories'),
    path('electronics_component',views.electronics_component, name='electronics_component'),
    path('computer_ssd',views.computer_ssd, name='computer_ssd'),
    path('graphics_card',views.graphics_card, name='graphics_card'),
    path('monitor',views.tablet_accessories, name='monitor'),
    path('pen_drive',views.pen_drive, name='pen_drive'),


    #home-appliances
    path('kitchen_appliances',views.kitchen_appliances, name='kitchen_appliances'),
    path('heater_fan_cooler',views.heater_fan_cooler, name='heater_fan_cooler'),
    path('lighting',views.lighting, name='lighting'),
    path('washing_machine',views.washing_machine, name='washing_machine'),
    path('regrigerator',views.regrigerator, name='regrigerator'),
    path('air_purifiers',views.air_purifiers, name='air_purifiers'),
    path('television',views.television, name='television'),
    path('microwave',views.microwave, name='microwave'),
    path('ait_conditioner',views.ait_conditioner, name='ait_conditioner'),
    path('air_cooler',views.air_cooler, name='air_cooler'),
]

