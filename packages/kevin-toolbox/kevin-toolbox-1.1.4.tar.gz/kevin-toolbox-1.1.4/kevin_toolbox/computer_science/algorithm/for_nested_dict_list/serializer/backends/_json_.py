import os
import json
from kevin_toolbox.data_flow.file import json_
from kevin_toolbox.data_flow.file.json_.converter import escape_non_str_dict_key, unescape_non_str_dict_key, \
    escape_tuple, unescape_tuple
from kevin_toolbox.computer_science.algorithm.for_nested_dict_list.serializer.backends import Backend_Base
from kevin_toolbox.computer_science.algorithm.for_nested_dict_list.serializer.variable import SERIALIZER_BACKEND


@SERIALIZER_BACKEND.register()
class Json_(Backend_Base):
    name = ":json"

    def write(self, name, var, **kwargs):
        assert self.writable(var=var)

        json_.write(content=var, file_path=os.path.join(self.paras["folder"], f'{name}.json'),
                    sort_keys=False, converters=[escape_non_str_dict_key, escape_tuple])
        return dict(backend=Json_.name, name=name)

    def read(self, name, **kwargs):
        assert self.readable(name=name)

        var = json_.read(file_path=os.path.join(self.paras["folder"], f'{name}.json'),
                         converters=[unescape_non_str_dict_key, unescape_tuple])
        return var

    def writable(self, var, **kwargs):
        """
            是否可以写
        """
        try:
            _ = json.dumps(var)
            return True
        except:
            return False

    def readable(self, name, **kwargs):
        """
            是否可以写
        """
        return os.path.isfile(os.path.join(self.paras["folder"], f'{name}.json'))


if __name__ == '__main__':
    backend = Json_(folder=os.path.join(os.path.dirname(__file__), "temp"))

    var_ = [{123: 123, None: None, "<eval>233": 233, "foo": (2, 3, 4)}, 233]
    print(backend.write(name=":inst", var=var_))

    b = backend.read(name=":inst")
    print(b)
