# AINFT-baby-shark-projects
A project to create a baby shark AINFT using LLM(Large Language Model).

### Create Your App and Connet AI Network
1. Create AIN Wallet
```python
from ain.ain import Ain

ain = Ain("https://testnet-api.ainetwork.ai", chainId=0)
# ain = Ain("https://mainnet-api.ainetwork.ai", chainId=1)

ain.wallet.create(1)
print(ain.wallet.accounts)
address = list(ain.wallet.accounts.keys())[0]

print("Address :", address)
print("Private Key:", ain.wallet.accounts[address].private_key)
print("Public Key:", ain.wallet.accounts[address].public_key)
```

2. Create APP
```python

import asyncio
import time

from ain.ain import Ain
from ain.types import ValueOnlyTransactionInput


ain = Ain("https://testnet-api.ainetwork.ai", chainId=0)
# ain = Ain("https://mainnet-api.ainetwork.ai", chainId=1)


address = "YOUR_ADDRESS"
private_key = "YOUR_PRIVATE_KEY"

ain.wallet.addAndSetDefaultAccount(private_key)


async def create_app(app_name):
    now = int(time.time() * 100)
    result = await ain.db.ref(f"/manage_app/{app_name}/create/{now}").setValue(
        ValueOnlyTransactionInput(
            value={
                "admin": {address: True},
                "service": {"stacking": {"lockup_duration": 604800000}},
            },
            nonce=-1,
        )
    )
    print(result)


loop = asyncio.get_event_loop()
loop.run_until_complete(create_app("YOUR_APP_NAME"))
```

3. Connect AINetwork