
from wkhtmltopdf.views import PDFTemplateView, PDFTemplateResponse
from django.core.context_processors import request
from django.shortcuts import render
from django.template import RequestContext 
from documentos.models import Expediente, Pase




class PaseReport(PDFTemplateView):
    
    filename = 'pase.pdf'
    template_name = 'pase_pdf.html'
    
    
    
    
    def generar(request, idExpediente, idPase):
        
#         return render(request, 'pase_pdf.html', {'pase':'Pase prueba'}, context_instance=RequestContext(request))
        template = 'pase_pdf.html'
#         something = get_object_or_404(Something,id=sID)
        expediente=[]
       
       
        expediente.append(Expediente.objects.get(numero = idExpediente))
        
        pase = Pase.objects.get(id=idPase)
        
        
        
        context = {
            'pase' : pase,
            'expediente' : expediente
            
        }
#         cmd_options = settings.WKHTMLTOPDF_CMD_OPTIONS
    
        return PDFTemplateResponse(request=request,
            context=context,
            template=template,
            filename='pase.pdf',
            show_content_in_browser=False)
        
        
        
        
        
        
        
        