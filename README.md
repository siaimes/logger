# 使用方法

入口python文件头部中填入以下四行：
```
import logging.config
from utils.logger import setup_logging
logger = logging.getLogger(__name__)
print = logger.info
```

入口处填入以下内容：

```
setup_logging(log_dir=log_dir)
```

`log_dir`可以根据任务来设置，例如，在每一个任务的配置文件中写入`config['log']['dir']`参数，注意，该路径中相关文件将被抹掉。

其他所有python文件头部填入以下内容：
```
import logging
logger = logging.getLogger(__name__)
print = logger.info
```

# 效果

所有日志输出到info.log(`logger.info(msg)`)或errors.log(`logger.error(msg)`)，并且标明该条日志来自哪一个文件。