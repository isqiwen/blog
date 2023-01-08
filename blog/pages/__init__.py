from blog.route import Route
from blog.pages.essays import *
from blog.pages.about import about
from blog.pages.cv import cv
from blog.pages.essay import essay
from blog.pages.gallery import gallery
from blog.pages.index import index
from blog.pages.tool import tool


routes = [r for r in locals().values() if isinstance(r, Route)]
