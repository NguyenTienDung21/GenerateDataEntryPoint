import json
from classes.application_map import  ApplicationMapData
from classes.variables import Variable
from classes.transition import Transition
from classes.path import PathOutputData
from variable_processing.lexer.grammar import parser


def extract_variables_from_json(json_data):
    variables = []
    for key, value in json_data.items():
        variable_name = value["name"]
        variables_format = parser.parse(value['value'])
        variable = Variable(variable_name, variables_format)
        variables.append(variable)
    return variables


def extract_variables(edge):
    action_type, action_data_json, action_target = edge.attribute
    if action_data_json is not None:
        action_data = json.loads(action_data_json)
        return extract_variables_from_json(action_data)

    return []

def traverse_json(json_data):
    application_map = ApplicationMapData(json_data)
    data = []
    for path in application_map.paths:
        transitions = []
        for edge in path.edges_list:
            variables = extract_variables(edge)
            id = edge.id
            transition = Transition(id, variables)
            transitions.append(transition)
        path_output_data = PathOutputData(path.id, transitions)
        data.append(path_output_data)
    # print(data)
    return str(data)


