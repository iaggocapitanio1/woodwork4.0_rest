# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import mimetypes
import os
from os.path import basename

from django.http import HttpResponse
from django.shortcuts import redirect, reverse
from django.views.static import serve

from bucket.models import File
from .settings import PROTECTED_MEDIA_LOCATION_PREFIX, PROTECTED_MEDIA_ROOT
from .utils import server_header

from django.contrib.auth.decorators import login_required
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@login_required
def protected_view(request, path, server="django", as_download=False):
    file = File.objects.filter(file=path).first()
    # if request.user.is_customer:
    #     if file.folder.user != request.user:
    #         return redirect(reverse("storages:error"))
    if server != "django":
        mimetype, encoding = mimetypes.guess_type(path)
        response = HttpResponse()
        response["Content-Type"] = mimetype
        if encoding:
            response["Content-Encoding"] = encoding

        if as_download:
            response["Content-Disposition"] = "attachment; filename={}".format(
                basename(path))

        # response[server_header(server)] = os.path.join(
        #     PROTECTED_MEDIA_LOCATION_PREFIX, path
        # ).encode("utf8")
        response['X-Accel-Redirect'] = os.path.join(
            PROTECTED_MEDIA_LOCATION_PREFIX, path
        ).encode("utf8")
    else:
        response = serve(
            request, path, document_root=PROTECTED_MEDIA_ROOT,
            show_indexes=False
        )

    logger.info(f"Response headers: {response.headers}")

    return response


# class PassthroughRenderer(renderers.BaseRenderer):
#     """
#         Return data as-is. View should supply a Response.
#     """
#     media_type = ''
#     format = ''
#
#     def render(self, data, accepted_media_type=None, renderer_context=None):
#         return data
#
#
# class ServerViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = File.objects.all()
#
#     def retrieve(self, request, *args, **kwargs):
#         file = File.objects.filter(file=args[0]).first()
#         if request.user.is_customer:
#             if file.folder.user != request.user:
#                 return redirect(reverse("storages:error"))
#
#     @action(methods=['get'], detail=True, renderer_classes=(PassthroughRenderer,))
#     def download(self, *args, **kwargs):
#         instance = self.get_object()
#
#         # get an open file handle (I'm just using a file attached to the model for this example):
#         file_handle = instance.file.open()
#
#         # send file
#         response = FileResponse(file_handle, content_type='whatever')
#         response['Content-Length'] = instance.file.size
#         response['Content-Disposition'] = 'attachment; filename="%s"' % instance.file.name
#
#         return response
