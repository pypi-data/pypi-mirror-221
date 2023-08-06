from __future__ import annotations

import json

import ckan.plugins.toolkit as tk
from ckanext.scheming.validation import scheming_validator, scheming_multiple_choice_output
from ckanext.toolbelt.decorators import Collector
from ckantoolkit import missing
from six import string_types

validator, get_validators = Collector("relationship").split()


@validator
@scheming_validator
def related_entity(field, schema):
    related_entity = field.get('related_entity')
    related_entity_type = field.get('related_entity_type')
    relation_type = field.get('relation_type')

    def validator(key, data, errors, context):
        if field.get('required') and data[key] is missing:
            errors[key].append(tk._('Select at least one'))

        entity_id = data.get(('id',))

        current_relations = _get_current_relations(entity_id, related_entity, related_entity_type, relation_type)
        selected_relations = _get_selected_relations(data[key])

        data[key] = json.dumps([value for value in selected_relations])

        add_relations = selected_relations - current_relations
        del_relations = current_relations - selected_relations

        data[('add_relations',)] = data.get(('add_relations',), [])
        data[('del_relations',)] = data.get(('del_relations',), [])

        data[('add_relations',)].extend([(rel, relation_type) for rel in add_relations])
        data[('del_relations',)].extend([(rel, relation_type) for rel in del_relations])

    return validator


def _get_current_relations(entity_id, related_entity, related_entity_type, relation_type):
    if entity_id:
        current_relations = tk.get_action('relationship_relations_list')({}, {'subject_id': entity_id,
                                                                              'object_entity': related_entity,
                                                                              'object_type': related_entity_type,
                                                                              'relation_type': relation_type})
        current_relations = [rel['object_id'] for rel in current_relations]
    else:
        current_relations = []
    return set(current_relations)


def _get_selected_relations(selected_relations):

    if isinstance(selected_relations, string_types) and "," in selected_relations:
        selected_relations = selected_relations.split(",")

    if selected_relations is not missing:
        selected_relations = scheming_multiple_choice_output(selected_relations)
        selected_relations = [] if selected_relations == [''] else selected_relations
    else:
        selected_relations = []
    return set(selected_relations)
