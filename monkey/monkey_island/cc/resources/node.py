import flask_restful
from flask import request

from monkey_island.cc.resources.auth.auth import jwt_required
from monkey_island.cc.resources.i_resource import IResource
from monkey_island.cc.services.node import NodeService


class Node(flask_restful.Resource, IResource):
    urls = ["/api/netmap/node"]

    @jwt_required
    def get(self):
        node_id = request.args.get("id")
        if node_id:
            return NodeService.get_displayed_node_by_id(node_id)

        return {}
