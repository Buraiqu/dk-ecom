from import_export import resources
from home.models import Customer

class CustomerResource(resources.ModelResource):
    class Meta:
        model = Customer
