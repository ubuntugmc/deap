from django.db import models

class StagingPharmacySales(models.Model):
    sale_id = models.IntegerField(primary_key=True)
    date = models.DateField()
    pharmacy_id = models.CharField(max_length=50)
    drug_name = models.CharField(max_length=200)
    drug_class = models.CharField(max_length=200)
    dose_mg = models.IntegerField()
    quantity_sold = models.IntegerField()
    patient_age = models.IntegerField()
    patient_gender = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'staging_pharmacy_sales'
