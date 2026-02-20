import opengradient as og
from opengradient.types import HistoricalInputQuery, CandleOrder, CandleType, SchedulerParams

# Initializing the client - it will use your config from ~/.opengradient_config.json
client = og.Client()

print("--- Starting Alpha Deployment on OpenGradient ---")

# 1. Define the Input Query for ETH/USD (as seen in docs)
input_query = HistoricalInputQuery(
    base="ETH",
    quote="USD",
    total_candles=10,
    candle_duration_in_mins=30,
    order=CandleOrder.ASCENDING,
    candle_types=[
        CandleType.OPEN,
        CandleType.HIGH,
        CandleType.LOW,
        CandleType.CLOSE
    ]
)

# 2. Set the execution schedule (Every 1 hour for 30 days)
scheduler_params = SchedulerParams(
    frequency=3600, 
    duration_hours=720 
)

# 3. Model CID for ETH Volatility (from official docs)
model_cid = "QmRhcpDXFYCKSinTmJYrAVM4Bbvck59Zb2onj3MHv9Kw5N"

print(f"Deploying workflow for Model: {model_cid}...")

try:
    # 4. Deploy the new workflow to the Alpha Testnet
    workflow_address = client.alpha.new_workflow(
        model_cid=model_cid,
        input_query=input_query,
        input_tensor_name="open_high_low_close",
        scheduler_params=scheduler_params
    )
    
    print("\n✅ DEPLOYMENT SUCCESSFUL!")
    print(f"Workflow Contract Address: {workflow_address}")
    print("Keep this address for your Discord ticket!")

except Exception as e:
    print(f"\n❌ Deployment Failed: {e}")
    print("Tip: Make sure your wallet has testnet tokens (SPG) from the faucet.")
