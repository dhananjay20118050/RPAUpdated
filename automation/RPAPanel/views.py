from RPAPanel.forms import NodesForm, HubsForm
from RPAPanel.models import Nodes, Hubs
from RPAPanel.models import query_nodes_by_args
from RPAPanel.serializers import NodeSerializer, HubSerializer
from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response


# Create your views here.
# Node View
def index(request):
    html = TemplateResponse(request, 'nodes/index.html')
    return HttpResponse(html.render())


def addnode(request):
    if request.method == 'POST':
        form = NodesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                # messages.success(request, 'Successfully Added')
                # return redirect('/Nodes')
                # response = {'status': 1, 'message': _("Ok")}
                return HttpResponse(json.dumps(response), content_type='application/json')
            except:
                pass
        else:
            messages.error(request, form.errors)
    else:
        form = NodesForm()
    return render(request, "nodes/add.html", {'form': form})


def edit(request, id):
    nodes = Nodes.objects.get(id=id)
    return render(request, 'nodes/edit.html', {'nodes': nodes})


def update(request, id):
    nodes = Nodes.objects.get(id=id)
    form = NodesForm(request.POST, instance=nodes)
    if form.is_valid():
        form.save()
        # return HttpResponseRedirect("/index")
        # return render(request, 'edit.html',{'users':users})

    return redirect('/index/')


def addprocess(request):
    if request.method == 'POST':
        form = NodesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                # messages.success(request, 'Successfully Added')
                # return redirect('/Nodes')
                # response = {'status': 1, 'message': _("Ok")}
                return HttpResponse(json.dumps(response), content_type='application/json')
            except:
                pass
        else:
            messages.error(request, form.errors)
    else:
        form = NodesForm()
    return render(request, "process/add.html", {'form': form})


# Create your views here.
class NodeViewSet(viewsets.ModelViewSet):
    queryset = Nodes.objects.all()
    serializer_class = NodeSerializer

    def list(self, request, **kwargs):
        try:
            users = query_nodes_by_args(**request.query_params)
            serializer = NodeSerializer(users['items'], many=True)
            result = dict()
            result['data'] = serializer.data
            result['draw'] = users['draw']
            result['recordsTotal'] = users['total']
            result['recordsFiltered'] = users['count']
            return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)

        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)


# Hub View
def indexhub(request):
    html = TemplateResponse(request, 'hubs/index.html')
    return HttpResponse(html.render())


class HubViewSet(viewsets.ModelViewSet):
    queryset = Hubs.objects.all()
    serializer_class = HubSerializer

    def list(self, request, **kwargs):
        try:
            users = query_nodes_by_args(**request.query_params)
            serializer = HubSerializer(users['items'], many=True)
            result = dict()
            result['data'] = serializer.data
            result['draw'] = users['draw']
            result['recordsTotal'] = users['total']
            result['recordsFiltered'] = users['count']
            return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)

        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)


def addhub(request):
    if request.method == 'POST':
        form = HubsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                # messages.success(request, 'Successfully Added')
                # return redirect('/Nodes')
                # response = {'status': 1, 'message': _("Ok")}
                return HttpResponse(json.dumps(response), content_type='application/json')
            except:
                pass
        else:
            messages.error(request, form.errors)
    else:
        form = HubsForm()
    return render(request, "hubs/add.html", {'form': form})


# Process View
def indexprocess(request):
    html = TemplateResponse(request, 'process/index.html')
    return HttpResponse(html.render())
