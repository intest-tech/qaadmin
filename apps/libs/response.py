from flask import jsonify

def json_response(data, status='success', error_msg='', **kwargs):
    """
    构建易处理的HTTP输出
    :param data: 
    :param status: 
    :param error_msg: 
    :param kwargs: 
    :return: 
    """
    if isinstance(data, dict):
        data.update(kwargs)
    response = dict(
        data=data,
        status=status,
        message=error_msg
    )
    return jsonify(response)