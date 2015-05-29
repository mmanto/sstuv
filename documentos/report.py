
from wkhtmltopdf.views import PDFTemplateView, PDFTemplateResponse
from django.core.context_processors import request
from django.shortcuts import render
from django.template import RequestContext 
from documentos.models import Expediente, Pase
import datetime




class PaseReport(PDFTemplateView):
    
    filename = 'pase.pdf'
    template_name = 'pase_pdf.html'
    
    
    
    
    def generar(request, idExpediente, idPase):
        
        template =  'pase_pdf.html'
           
        expediente=[]
        expediente.append(Expediente.objects.get(id = idExpediente))
        
        pase = Pase.objects.get(id=idPase)
        
        dateNow = datetime.datetime.now()
        
#         dateCurrent = dateNow.day + "/" + dateNow.month + "/" + dateNow.year
        dateCurrent = "%s/%s/%s" % (dateNow.day, dateNow.month, dateNow.year) 
         
        context = {
            'pase' : pase,
            'expediente' : expediente,
            'dateCurrent' : dateCurrent
            
        }
#         cmd_options = settings.WKHTMLTOPDF_CMD_OPTIONS
    
        return PDFTemplateResponse(request=request,
            context=context,
            template=template,
            show_content_in_browser=True, 
            )

        
        
        
        
        
        
        
        