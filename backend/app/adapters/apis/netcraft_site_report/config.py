from pydantic import BaseModel


class NetcraftSiteReportConfig(BaseModel):
    base_url: str = "https://sitereport.netcraft.com"
    endpoint: str = "https://sitereport.netcraft.com/?url={url}"
    rate_limit: str = "Unlimited / Free"
    website: str = "https://sitereport.netcraft.com"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
