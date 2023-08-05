# rust-github-flow-test
test rust PyO3 github flow


```bash
pip install zzq-string-sum
```

use it in python

```python
from zzq_string_sum import databus


print("zzq see ", databus.sum_as_string(1, 2))
print("zzq see2 ", databus.sum_as_string(10, 20))

databus.init("http://loaclhost:8080")
```