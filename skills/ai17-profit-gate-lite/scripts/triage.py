"""AI-17 Lite: local basic triage, without profit or estimation logic."""
import argparse,json
from pathlib import Path
FIELDS=("scope","systems","volume","access","data_boundary","acceptance","deployment_owner","maintenance_owner","deadline","budget")
def triage(data):
    if not isinstance(data,dict): raise ValueError("Input must be an object")
    brief=data.get("brief",{})
    if not isinstance(brief,dict): raise ValueError("brief must be an object")
    normalized={k:brief.get(k) for k in FIELDS}
    gaps=[k for k,v in normalized.items() if v is None or v=="" or v==[] or v=="unknown"]
    blockers=data.get("confirmed_blockers",[])
    if not isinstance(blockers,list) or any(not isinstance(b,str) or not b.strip() for b in blockers): raise ValueError("confirmed_blockers must be a list of evidenced descriptions")
    reviewed=data.get("basic_checks_confirmed") is True
    decision="SKIP" if blockers else "REVIEW" if gaps or not reviewed else "PASS"
    checklist=["Confirm authority and supported integration actions", "Identify sensitive data and access boundaries", "Agree acceptance and failure handling", "Assign deployment and maintenance owners", "Verify budget, deadline and recurring usage responsibility"]
    return {"edition":"Lite","version":"1.0.0","decision":decision,"meaning":"Basic triage only; PASS means ready for deeper assessment, not approval to quote or deploy","normalized_brief":normalized,"requirement_gaps":gaps,"risk_checklist":checklist,"confirmed_blockers":blockers,"quote_allowed":False,"next_actions":(blockers or ["Clarify "+x for x in gaps] or (["Confirm the basic checks with evidence"] if not reviewed else ["Complete evidence and economics assessment before committing"]))[:3]}
if __name__=="__main__":
    parser=argparse.ArgumentParser();parser.add_argument("input");args=parser.parse_args()
    try: result=triage(json.loads(Path(args.input).read_text(encoding="utf-8-sig")))
    except (ValueError,OSError) as e: parser.exit(2,"Invalid brief: "+str(e)+"\n")
    print(json.dumps(result,ensure_ascii=False,indent=2))
