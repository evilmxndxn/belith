from pydantic import BaseModel


class WikidataSparqlConfig(BaseModel):
    base_url: str = "https://query.wikidata.org"
    endpoint: str = "https://query.wikidata.org/sparql?query={SPARQL}"
    rate_limit: str = "Fair use"
    website: str = "https://query.wikidata.org"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
