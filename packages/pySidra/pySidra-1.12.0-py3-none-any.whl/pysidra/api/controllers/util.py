import inspect
import json
import time
from typing import List, Dict

import requests

from pysidra.api.controllers import Constants


def time_format(m):
    return time.strftime("%I-%M-%S-%p", time.localtime(m))


def get_request_params(var):
    return {
        k: v
        for k, v in var
        if k not in Constants.ATTRIBUTES_TO_AVOID_IN_PARAMS and v is not None
    }


def check_file(response):
    resp_status = response.status_code
    result_text = response.text

    if resp_status == 200:
        try:
            result_status = json.loads(result_text)["executionStatus"]["lifecycleState"]
            return result_text, result_status
        except:
            raise InterruptedError(
                'While generating file "resultState" was not found: {} {}'.format(
                    resp_status, result_text
                )
            )
    else:
        raise InterruptedError(
            "While generating file: {} {}".format(resp_status, result_text)
        )


def make_columns_list(responseText):
    columns = []
    for i in responseText:
        columns.append(i["name"])
    column_list = ",".join(columns)
    return column_list


def get_resp_status(resp):
    if resp.status_code == 200:
        print("status_code = 200, Success")
    else:
        print("status_code = {} {}".format(resp.status_code, resp.text))


def get_url():
    """
    Get url from constants list according to the class and method from where get_url() is called.
    """
    stack = inspect.stack()

    for i in range(1, 3):
        i_frame = stack[i][0]
        url_class = i_frame.f_locals["self"].__class__.__name__
        url_method = i_frame.f_code.co_name
        url = "URL_{0}_{1}".format(url_class.upper(), url_method.upper())
        url_dict = vars(Constants)
        if url in url_dict:
            return url_dict[url]


def get_response(url, method="GET", token=None, headers=None, params=None, data=None):
    if headers is None:
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        headers.update({"Authorization": "Bearer {}".format(token)})

    if params is None:
        params = {}
    params.update({"api-version": Constants.API_VERSION})
    if headers == {"Content-Type": "application/json"}:
        headers.update({"Authorization": "Bearer {}".format(token)})

    try:
        resp = requests.request(
            method, url=url, headers=headers, params=params, data=data
        )
        resp.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    if Constants.DEBUG_REQUEST_RESPONSE:
        get_resp_status(resp)
    return resp


def prepare_dict_from_obj(
        class_object: object,
        copy: bool = True,
        exclude: List = None,
        emptyStrIfNone: bool = False,
        excludeNone: bool = False
) -> Dict:

    if class_object is None:
        result = {}
    else:
        result = class_object.__dict__.copy() if copy else class_object.__dict__

        if exclude is not None:
            for key in exclude:
                if key in result:
                    del result[key]
                else:
                    raise ValueError("Key {} is not in object {}".format(key, result))

        if excludeNone:
            result = {k: v for k, v in result.items() if v is not None}
        elif emptyStrIfNone:
            result = {k: "" if v is None else v for k, v in result.items()}

    return result
