from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .forms import UploadPDFForm
from PyPDF2 import PdfReader


# start
# import PyPDF2
from transformers import pipeline



def answer_question(request):

    
    if request.method == 'POST':

        num1 = request.POST.get('num1')
        
        pdf_text = request.POST.get('contentv', '')
        #pdf_text = upload_pdf(request)
        
      #  modified_data = get_pdf_content(pdf_text)
     
        
        #c= f"{num1} {modified_data}"
     

        qa_pipeline = pipeline('question-answering', model='bert-large-uncased-whole-word-masking-finetuned-squad')
        result = qa_pipeline(question=num1, context=pdf_text)
        ans=result['answer']
        #return render(request, 'pdfapp/index.html', {'result': "pdf_textrtyt"})
        return render(request, 'pdfapp/index.html', {'result':ans, 'content':pdf_text})

    return HttpResponse('Method Not Allowed', status=405)







def upload_pdf(request):
    if request.method == 'POST':
        #pass
        form = UploadPDFForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = form.cleaned_data['file']
            pdf_reader = PdfReader(pdf_file)
            num_pages = len(pdf_reader.pages)
            content = ''
            for page_num in range(num_pages):
              #  page = pdf_reader.getPage(page_num)
                page = pdf_reader.pages[page_num]
                
                #content += page.extractText()
                content += page.extract_text()
                
                
            return render(request, 'pdfapp/index.html', {'content': content})
    else:
        form = UploadPDFForm()
    return render(request, 'pdfapp/index.html', {'form': form})

