import xml.etree.ElementTree as ET
from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    return render(request, 'index.html')


def search(request):
    target_attrib = []
    file_not_found_msg=''
    if request.method == 'POST':
        try:
            filename = request.POST['search'] + '.xml'
            tree_data = ET.parse(filename)
            root_element = tree_data.getroot()
            target_element = root_element.findall(".//Annual/")

            for each_child in target_element:
                for each_attribute in each_child.attrib:
                    if each_attribute == 'expectDate':
                        target_attrib.append(each_child.get(each_attribute))
            if not target_attrib:
                target_attrib.append("No data in the file")
            return render(request, 'index.html', {'target_attrib': target_attrib})
            #return render(request, 'index.html', {'target_attrib': target_attrib})
        except FileNotFoundError:
            file_not_found_msg = 'File not found'
            return render(request, 'index.html', {'file_not_found_msg': file_not_found_msg})
    else:
        return render(request, 'index.html',{'file_not_found_msg': file_not_found_msg})

        #return render(request, 'search.html', {'target_attrib': target_attrib})
