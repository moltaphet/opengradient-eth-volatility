import os
import opengradient as og
from opengradient.types import HistoricalInputQuery, CandleOrder, CandleType

os.environ["OPENGRADIENT_ENV"] = "alpha"

PRIVATE_KEY = "YOUR PRIVATE_KEY " 

print("--- Starting OpenGradient Alpha Deployment ---")

try:
    client = og.Client(private_key=PRIVATE_KEY)
    
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

    print("Action: Deploying AI Workflow...")
    
    # Model CID from the official Alpha list
    model_cid = "QmRhcpDXFYCKSinTmJYrAVM4Bbvck59Zb2onj3MHv9Kw5N"

    # Deploying the workflow
    workflow_address = client.alpha.new_workflow(
        model_cid=model_cid,
        input_query=input_query,
        input_tensor_name="open_high_low_close",
        scheduler_params={
            "frequency": 3600, 
            "duration_hours": 24
        }
    )
    
    print("\n" + "="*40)
    print("DEPLOYMENT SUCCESSFUL!")
    print(f"Workflow Address: {workflow_address}")
    print("="*40)
    print("\nCopy the address above for your Discord ticket.")

except Exception as e:
    print(f"\nDeployment Error: {e}")

