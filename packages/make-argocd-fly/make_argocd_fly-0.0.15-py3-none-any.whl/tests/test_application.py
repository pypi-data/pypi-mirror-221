import pytest

from make_argocd_fly.application import Application
from make_argocd_fly.resource import ResourceViewer


def test_application_creation():
  app_viewer_name = 'tmp'
  app_viewer = ResourceViewer('/tmp')
  app_viewer.name = app_viewer_name
  env_name = 'dev_environment'
  template_vars = {}
  app = Application(app_viewer, env_name, template_vars)

  assert app.app_viewer == app_viewer
  assert app.env_name == env_name
  assert app.template_vars == template_vars
  assert app.name == app_viewer_name
