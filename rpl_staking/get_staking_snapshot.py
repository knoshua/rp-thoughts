import os

import pandas as pd
from web3 import HTTPProvider, Web3

API_KEY = os.environ['INFURA']
CLIENT = Web3(HTTPProvider(f"https://mainnet.infura.io/v3/{API_KEY}"))

RocketNodeManager = CLIENT.eth.contract(
    address=Web3.to_checksum_address("0x89F478E6Cc24f052103628f36598D4C14Da3D287"),
    abi=
    '[{"inputs":[{"internalType":"contract RocketStorageInterface","name":"_rocketStorageAddress","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"node","type":"address"},{"indexed":false,"internalType":"uint256","name":"time","type":"uint256"}],"name":"NodeRegistered","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"node","type":"address"},{"indexed":false,"internalType":"uint256","name":"network","type":"uint256"}],"name":"NodeRewardNetworkChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"node","type":"address"},{"indexed":false,"internalType":"bool","name":"state","type":"bool"}],"name":"NodeSmoothingPoolStateChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"node","type":"address"},{"indexed":false,"internalType":"uint256","name":"time","type":"uint256"}],"name":"NodeTimezoneLocationSet","type":"event"},{"inputs":[{"internalType":"address","name":"_nodeAddress","type":"address"}],"name":"getAverageNodeFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_nodeAddress","type":"address"}],"name":"getFeeDistributorInitialised","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_offset","type":"uint256"},{"internalType":"uint256","name":"_limit","type":"uint256"}],"name":"getNodeAddresses","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_index","type":"uint256"}],"name":"getNodeAt","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getNodeCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_offset","type":"uint256"},{"internalType":"uint256","name":"_limit","type":"uint256"}],"name":"getNodeCountPerTimezone","outputs":[{"components":[{"internalType":"string","name":"timezone","type":"string"},{"internalType":"uint256","name":"count","type":"uint256"}],"internalType":"struct RocketNodeManagerInterface.TimezoneCount[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_nodeAddress","type":"address"}],"name":"getNodeDetails","outputs":[{"components":[{"internalType":"bool","name":"exists","type":"bool"},{"internalType":"uint256","name":"registrationTime","type":"uint256"},{"internalType":"string","name":"timezoneLocation","type":"string"},{"internalType":"bool","name":"feeDistributorInitialised","type":"bool"},{"internalType":"address","name":"feeDistributorAddress","type":"address"},{"internalType":"uint256","name":"rewardNetwork","type":"uint256"},{"internalType":"uint256","name":"rplStake","type":"uint256"},{"internalType":"uint256","name":"effectiveRPLStake","type":"uint256"},{"internalType":"uint256","name":"minimumRPLStake","type":"uint256"},{"internalType":"uint256","name":"maximumRPLStake","type":"uint256"},{"internalType":"uint256","name":"ethMatched","type":"uint256"},{"internalType":"uint256","name":"ethMatchedLimit","type":"uint256"},{"internalType":"uint256","name":"minipoolCount","type":"uint256"},{"internalType":"uint256","name":"balanceETH","type":"uint256"},{"internalType":"uint256","name":"balanceRETH","type":"uint256"},{"internalType":"uint256","name":"balanceRPL","type":"uint256"},{"internalType":"uint256","name":"balanceOldRPL","type":"uint256"},{"internalType":"uint256","name":"depositCreditBalance","type":"uint256"},{"internalType":"uint256","name":"distributorBalanceUserETH","type":"uint256"},{"internalType":"uint256","name":"distributorBalanceNodeETH","type":"uint256"},{"internalType":"address","name":"withdrawalAddress","type":"address"},{"internalType":"address","name":"pendingWithdrawalAddress","type":"address"},{"internalType":"bool","name":"smoothingPoolRegistrationState","type":"bool"},{"internalType":"uint256","name":"smoothingPoolRegistrationChanged","type":"uint256"},{"internalType":"address","name":"nodeAddress","type":"address"}],"internalType":"struct NodeDetails","name":"nodeDetails","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_nodeAddress","type":"address"}],"name":"getNodeExists","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_nodeAddress","type":"address"}],"name":"getNodePendingWithdrawalAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_nodeAddress","type":"address"}],"name":"getNodeRegistrationTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_nodeAddress","type":"address"}],"name":"getNodeTimezoneLocation","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_nodeAddress","type":"address"}],"name":"getNodeWithdrawalAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_nodeAddress","type":"address"}],"name":"getRewardNetwork","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_offset","type":"uint256"},{"internalType":"uint256","name":"_limit","type":"uint256"}],"name":"getSmoothingPoolRegisteredNodeCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_nodeAddress","type":"address"}],"name":"getSmoothingPoolRegistrationChanged","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_nodeAddress","type":"address"}],"name":"getSmoothingPoolRegistrationState","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"initialiseFeeDistributor","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_timezoneLocation","type":"string"}],"name":"registerNode","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_nodeAddress","type":"address"},{"internalType":"uint256","name":"_network","type":"uint256"}],"name":"setRewardNetwork","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"_state","type":"bool"}],"name":"setSmoothingPoolRegistrationState","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_timezoneLocation","type":"string"}],"name":"setTimezoneLocation","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"version","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"}]'
)

RocketNodeStaking = CLIENT.eth.contract(
    address=Web3.to_checksum_address("0x0d8D8f8541B12A0e1194B7CC4b6D954b90AB82ec"),
    abi=
    '[{"inputs":[{"internalType":"contract RocketStorageInterface","name":"_rocketStorageAddress","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"node","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"ethValue","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"time","type":"uint256"}],"name":"RPLSlashed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"time","type":"uint256"}],"name":"RPLStaked","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"time","type":"uint256"}],"name":"RPLWithdrawn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"node","type":"address"},{"indexed":true,"internalType":"address","name":"caller","type":"address"},{"indexed":false,"internalType":"bool","name":"allowed","type":"bool"},{"indexed":false,"internalType":"uint256","name":"time","type":"uint256"}],"name":"StakeRPLForAllowed","type":"event"},{"inputs":[{"internalType":"address","name":"_nodeAddress","type":"address"}],"name":"getNodeETHCollateralisationRatio","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_nodeAddress","type":"address"}],"name":"getNodeETHMatched","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_nodeAddress","type":"address"}],"name":"getNodeETHMatchedLimit","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_nodeAddress","type":"address"}],"name":"getNodeETHProvided","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_nodeAddress","type":"address"}],"name":"getNodeEffectiveRPLStake","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_nodeAddress","type":"address"}],"name":"getNodeMaximumRPLStake","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_nodeAddress","type":"address"}],"name":"getNodeMinimumRPLStake","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_nodeAddress","type":"address"}],"name":"getNodeRPLStake","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_nodeAddress","type":"address"}],"name":"getNodeRPLStakedTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getTotalRPLStake","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_caller","type":"address"},{"internalType":"bool","name":"_allowed","type":"bool"}],"name":"setStakeRPLForAllowed","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_nodeAddress","type":"address"},{"internalType":"uint256","name":"_ethSlashAmount","type":"uint256"}],"name":"slashRPL","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"stakeRPL","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_nodeAddress","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"stakeRPLFor","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"version","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"withdrawRPL","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
)

RocketNetworkPrices = CLIENT.eth.contract(
    address=Web3.to_checksum_address("0x751826b107672360b764327631cC5764515fFC37"),
    abi=
    '[{"inputs":[{"internalType":"contract RocketStorageInterface","name":"_rocketStorageAddress","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":false,"internalType":"uint256","name":"block","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"rplPrice","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"time","type":"uint256"}],"name":"PricesSubmitted","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"block","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"rplPrice","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"time","type":"uint256"}],"name":"PricesUpdated","type":"event"},{"inputs":[{"internalType":"uint256","name":"_block","type":"uint256"},{"internalType":"uint256","name":"_rplPrice","type":"uint256"}],"name":"executeUpdatePrices","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getLatestReportableBlock","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getPricesBlock","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getRPLPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_block","type":"uint256"},{"internalType":"uint256","name":"_rplPrice","type":"uint256"}],"name":"submitPrices","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"version","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"}]'
)

if __name__ == '__main__':
    num_nodes = RocketNodeManager.functions.getNodeCount().call()

    rpl_price_in_eth = RocketNetworkPrices.functions.getRPLPrice().call() / 1e18
    provided_eth_ls = []
    matched_eth_ls = []
    staked_rpl_value_in_eth_ls = []

    for offset in range(0, num_nodes, 100):
        print(offset)
        node_ls = RocketNodeManager.functions.getNodeAddresses(offset, 100).call()
        for addr in node_ls:
            provided_eth_ls.append(RocketNodeStaking.functions.getNodeETHProvided(addr).call())
            matched_eth_ls.append(RocketNodeStaking.functions.getNodeETHMatched(addr).call())
            rpl_stake = RocketNodeStaking.functions.getNodeRPLStake(addr).call()
            staked_rpl_value_in_eth_ls.append(rpl_stake * rpl_price_in_eth)

    df = pd.DataFrame({
        'staked_rpl_value_in_eth': staked_rpl_value_in_eth_ls,
        'provided_eth': provided_eth_ls,
        'matched_eth': matched_eth_ls
    })
    df /= 1e18
    df.to_csv('staking_snapshot.csv')