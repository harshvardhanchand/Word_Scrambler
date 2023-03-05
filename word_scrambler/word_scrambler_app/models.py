from django.db import models

from django.core.serializers.json import DjangoJSONEncoder
class TrieNode(models.Model):
    """A model representing a node in a trie data structure."""
    children = models.JSONField(default=dict)
    words = models.JSONField(default=list)


class Trie(models.Model):
    """A model representing a trie data structure."""
    root = models.ForeignKey(TrieNode, on_delete=models.CASCADE)





class TrieNodeEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, TrieNode):
            return {'key': obj.key, 'value': obj.value}
        return super().default(obj)

class TrieEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Trie):
            return {'root': obj.root, 'size': obj.size}
        return super().default(obj)