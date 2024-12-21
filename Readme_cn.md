# NodepayChecker 

自动化的 Nodepay 多账号 Airdrop 检查器。通过此 Python 脚本，您可以管理多个 Nodepay 账户并安全地查看积分，非常适合拥有多个 Nodepay 账号的用户！

# 功能

1. 检查所有 Nodepay 账户的空投（Airdrop）金额，并将结果记录在 `log.txt` 文件中。  
2. 程序结束后，自动汇总所有账户的代币总量。

# 使用步骤

1. `git clone https://github.com/Solana0x/NodepayChecker`
2. `cd NodepayChecker`
3. `pip install requests`
4. 在 `tokens.txt` 文件中添加 Nodepay 账户的最新 Token（请注意 Token 每 15 天会重置一次）。
5. 在 `proxy.txt` 文件中添加代理，格式示例：`http://username:password@ip:port`
6. 运行 `python check.py`
7. 脚本将自动获取所有 Nodepay 账户的空投积分，并将响应保存到 `log.txt` 文件中。

## 如需帮助，请联系：`0xphatom` (Discord) 
[https://discord.com/users/979641024215416842](https://discord.com/users/979641024215416842)

# 社交平台

- **Telegram** - [https://t.me/phantomoalpha](https://t.me/phantomoalpha)
- **Discord** - [https://discord.gg/pGJSPtp9zz](https://discord.gg/pGJSPtp9zz)
