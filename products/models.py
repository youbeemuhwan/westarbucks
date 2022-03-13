from django.db import models



class category(models.Model) :
    #id = models.IntegerField(primary_key = True)
   
    # 만약 기본키를 지정하지 않은 상태에서 테이블을 생성하면 테이블 생성 시에 자동으로 Pk 생성
    name = models.CharField(max_length = 50)
    menu_id= models.ForeignKey("menu", on_delete=models.PROTECT)

    class Meta:
        db_table = 'products_category'


class menu(models.Model) :
    #id = models.IntegerField(primary_key = True)
    
    name = models.CharField(max_length = 50)
    
    class META:
        db_table = 'products_menu'

    
class drinks(models.Model) :
    #id = models.IntegerField(primary_key = True)
    
    category_id= models.ForeignKey("category",  on_delete=models.PROTECT)
    korean_name = models.CharField(max_length = 45)
    english_name = models.CharField(max_length = 45)
    description = models.TextField()
    models.CharField(max_length=50)
    
    class Meta:
        db_table = 'products_drinks'

    
    
class allergy_drink(models.Model) :
    #id = models.IntegerField(primary_key = True)
    
    allergy_id= models.ForeignKey("allergy", on_delete = models.PROTECT)
    drink_id= models.ForeignKey("drinks", on_delete = models.PROTECT)
   
    class Meta:
        db_table = 'products_allergy_drink'

    

class nutritions (models.Model) :
     #id = models.IntegerField(primary_key = True)
    
    one_serving_kca = models.DecimalField(max_digits = 10, decimal_places = 2, null = True)
    sodium_mg = models.DecimalField(max_digits = 10, decimal_places = 2, null = True)
    saturated_fat_g = models.DecimalField(max_digits = 10, decimal_places = 2, null = True)
    sugars_g = models.DecimalField(max_digits = 10, decimal_places = 2, null = True)
    protein_g = models.DecimalField(max_digits = 10, decimal_places = 2, null = True)
    caffeine_mg = models.DecimalField(max_digits = 10, decimal_places = 2, null = True)
    drink_id = models.ForeignKey("drinks", on_delete=models.PROTECT, null = True)
    size_id = models.ForeignKey("sizes", on_delete=models.PROTECT, null = True)
    
    class Meta:
        db_table = 'products_nutritions'



class images (models.Model) :
    
    image_url = models.CharField(max_length=2000) # 이미지도 링크이기에 charfield 형식으로 저장 하는 건가?
    drink_id= models.ForeignKey("drinks", on_delete=models.PROTECT)
    
    class Meta:
        db_table = 'products_images'
        
class allergy (models.Model) :
    
    name = models.CharField(max_length = 45)
    
    class Meta:
        db_table = 'product_allergy'
    
    
class sizes(models.Model) :
    
    name = models.CharField(max_length = 45)
    size_mi = models.CharField(max_length = 45, null = True)
    size_fluid_ounce = models.CharField(max_length = 45, null = True)
    
    class Meta:
        db_table = 'product_sizes'
    
    

# Create your models here.

