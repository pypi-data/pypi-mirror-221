from django.contrib.auth.mixins import PermissionRequiredMixin
from netbox.views import generic
from . import forms, models, tables, filtersets
#from rest_framework import status, viewsets
#from rest_framework.response import Response


### Vendor
class VendorView(PermissionRequiredMixin, generic.ObjectView):
    permission_required = ('dcim.view_site', 'dcim.view_device')
    queryset = models.Vendor.objects.all()


class VendorListView(PermissionRequiredMixin, generic.ObjectListView):
    permission_required = ('dcim.view_site', 'dcim.view_device')
    queryset = models.Vendor.objects.all()
    table = tables.VendorTable
    filterset = filtersets.VendorFilterSet
    filterset_form = forms.VendorFilterForm


class VendorEditView(PermissionRequiredMixin, generic.ObjectEditView):
    permission_required = ('dcim.view_site', 'dcim.view_device')
    queryset = models.Vendor.objects.all()
    form = forms.VendorForm

    template_name = 'netbox_software/vendor_edit.html'


class VendorDeleteView(PermissionRequiredMixin, generic.ObjectDeleteView):
    permission_required = ('dcim.view_site', 'dcim.view_device')
    queryset = models.Vendor.objects.all()


### SoftwareType
class SoftwareTypeView(PermissionRequiredMixin, generic.ObjectView):
    permission_required = ('dcim.view_site', 'dcim.view_device')
    queryset = models.SoftwareType.objects.all()


class SoftwareTypeListView(PermissionRequiredMixin, generic.ObjectListView):
    permission_required = ('dcim.view_site', 'dcim.view_device')
    queryset = models.SoftwareType.objects.all()
    table = tables.SoftwareTypeTable
    filterset = filtersets.SoftwareTypeFilterSet
    filterset_form = forms.SoftwareTypeFilterForm


class SoftwareTypeEditView(PermissionRequiredMixin, generic.ObjectEditView):
    permission_required = ('dcim.view_site', 'dcim.view_device')
    queryset = models.SoftwareType.objects.all()
    form = forms.SoftwareTypeForm

    template_name = 'netbox_software/softwaretype_edit.html'

#    def create(self, request, *args, **kwargs):
#        serializer = self.get_serializer(data=request.data, many=isinstance(request.data,list))
#        serializer.is_valid(raise_exception=True)
#        self.perform_create(serializer)
#        headers=self.get_success_headers(serializer.data)
#        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class SoftwareTypeDeleteView(PermissionRequiredMixin, generic.ObjectDeleteView):
    permission_required = ('dcim.view_site', 'dcim.view_device')
    queryset = models.SoftwareType.objects.all()


### Application
class ApplicationView(PermissionRequiredMixin, generic.ObjectView):
    permission_required = ('dcim.view_site', 'dcim.view_device')
    queryset = models.Application.objects.all()


class ApplicationListView(PermissionRequiredMixin, generic.ObjectListView):
    permission_required = ('dcim.view_site', 'dcim.view_device')
    queryset = models.Application.objects.all()
    table = tables.ApplicationTable
    filterset = filtersets.ApplicationFilterSet
    filterset_form = forms.ApplicationFilterForm


class ApplicationEditView(PermissionRequiredMixin, generic.ObjectEditView):
    permission_required = ('dcim.view_site', 'dcim.view_device')
    queryset = models.Application.objects.all()
    form = forms.ApplicationForm

    template_name = 'netbox_software/application_edit.html'


class ApplicationDeleteView(PermissionRequiredMixin, generic.ObjectDeleteView):
    permission_required = ('dcim.view_site', 'dcim.view_device')
    queryset = models.Application.objects.all()


### ApplicationVersion
class ApplicationVersionView(PermissionRequiredMixin, generic.ObjectView):
    permission_required = ('dcim.view_site', 'dcim.view_device')
    queryset = models.ApplicationVersion.objects.all()


class ApplicationVersionListView(PermissionRequiredMixin, generic.ObjectListView):
    permission_required = ('dcim.view_site', 'dcim.view_device')
    queryset = models.ApplicationVersion.objects.all()
    table = tables.ApplicationVersionTable
    filterset = filtersets.ApplicationVersionFilterSet
    filterset_form = forms.ApplicationVersionFilterForm


class ApplicationVersionEditView(PermissionRequiredMixin, generic.ObjectEditView):
    permission_required = ('dcim.view_site', 'dcim.view_device')
    queryset = models.ApplicationVersion.objects.all()
    form = forms.ApplicationVersionForm

    template_name = 'netbox_software/applicationversion_edit.html'


class ApplicationVersionDeleteView(PermissionRequiredMixin, generic.ObjectDeleteView):
    permission_required = ('dcim.view_site', 'dcim.view_device')
    queryset = models.ApplicationVersion.objects.all()


### DeviceSoftware
class DeviceSoftwareView(PermissionRequiredMixin, generic.ObjectView):
    permission_required = ('dcim.view_site', 'dcim.view_device')
    queryset = models.DeviceSoftware.objects.all()


class DeviceSoftwareListView(PermissionRequiredMixin, generic.ObjectListView):
    permission_required = ('dcim.view_site', 'dcim.view_device')
    queryset = models.DeviceSoftware.objects.all()
    table = tables.DeviceSoftwareTable
    filterset = filtersets.DeviceSoftwareFilterSet
    filterset_form = forms.DeviceSoftwareFilterForm


class DeviceSoftwareEditView(PermissionRequiredMixin, generic.ObjectEditView):
    permission_required = ('dcim.view_site', 'dcim.view_device')
    queryset = models.DeviceSoftware.objects.all()
    form = forms.DeviceSoftwareForm

    template_name = 'netbox_software/devicesoftware_edit.html'


class DeviceSoftwareDeleteView(PermissionRequiredMixin, generic.ObjectDeleteView):
    permission_required = ('dcim.view_site', 'dcim.view_device')
    queryset = models.DeviceSoftware.objects.all()
