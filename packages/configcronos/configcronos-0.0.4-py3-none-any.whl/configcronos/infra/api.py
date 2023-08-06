import datetime

from configcronos.core.usecases import ClientService, DatabaseService, SegmentService, PingerService, Phase2Service, SQLsService, ScheduleService
from configcronos.infra.repositories import ClientRepositoryAPI, DatabaseRepositoryAPI, SegmentRepositoryAPI, PingerRepositoryAPI, Phase2RepositoryAPI, SQLsRepositoryAPI, ScheduleRepositoryAPI, AuthRepositoryAPI
from configcronos.core.entities import Client, Database, Segment, Phase2, Oracle, SQLs, Schedule

HEADERS = None
EXP_TIME = None


def authenticate(username: str, password: str, client_id: str) -> None:
    global HEADERS

    if token == "DEBUGETL":
        #HEADERS = {"Authorization": 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjE2NjcyNDg1MTAtMTZiNzljZTQtNDM1YS00YzA2LTkxZDItZjBjNjk5MzEyNjNkIiwidHlwIjoiSldUIn0.eyJzdWIiOiIxNTkiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJkYXZpX3NtYXJrZXQiLCJlbWFpbCI6ImRhdmlAc21hcmtldHNvbHV0aW9ucy5jb20uYnIiLCJjbGllbnRfaWQiOiJvbmJvYXJkaW5nIiwic3RvcmVzIjpbIjEiLCIxMCIsIjIiLCIyMDEiLCIyMDMiLCIyMiIsIjMiLCIzMDEiLCI0IiwiNSIsIjYiLCI3IiwiOCIsIjkiLCI5MDEiXSwicm9sZXMiOlsiYXByb3ZhY2FvIiwicmVsYXRvcmlvcyIsImRpYWdyYW1hZG9yIiwiZWRpdGFyX21hcGFzIiwibGlzdGFyX2Fjb2VzIiwibGlzdGFyX21hcGFzIiwiY29uZmlndXJhY29lcyIsImVkaXRhcl9jYXJ0YXoiLCJjYW5jZWxhcl9vZmVydGEiLCJkdXBsaWNhcl9vZmVydGEiLCJnZXJlbmNpYXJfYWNvZXMiLCJnZXJlbmNpYXJfYXJlYXMiLCJiYW5jb19kZV9pbWFnZW5zIiwiY3JpYXJfYXRpdmlkYWRlcyIsImVkaXRhcl9kZXNjcmljYW8iLCJnZXJlbmNpYXJfdG9rZW5zIiwibGlzdGFyX2NhbXBhbmhhcyIsInZlcl9sb2dzX29mZXJ0YXMiLCJnZXJlbmNpYXJfb2ZlcnRhcyIsInBlcmZpbF9wZXJtaXNzb2VzIiwiYXVkaXRhcl9hdGl2aWRhZGVzIiwiY3JpYXJfZWRpdGFyX2NpY2xvIiwiZWRpdGFyX3RleHRvX2xlZ2FsIiwiZ2VyZW5jaWFyX2NhcnRhemVzIiwiZ2VyZW5jaWFyX3VzdWFyaW9zIiwiZ2VyZW5jaWFyX2NhbXBhbmhhcyIsImdlcmVuY2lhcl9jb250cmF0b3MiLCJnZXJlbmNpYXJfZXRpcXVldGFzIiwiYWx0ZXJhcl9wcm9kdXRvX2FjYW8iLCJhbHRlcmFyX3Jlc3BvbnNhdmVpcyIsImdlcmVuY2lhcl90aXBvX2RlX2FyZWEiLCJlZGl0YXJfZGVzY3JpY2FvX2NhcnRheiIsImdlcmVuY2lhcl9wYXN0YXNfY2FydGF6Iiwic21hcmtldGZ5X2F0aXZvX3VzdWFyaW8iLCJhcHJvdmFyX29mZXJ0YXNfaW50ZXJuYXMiLCJ2aXN1YWxpemFyX2NpY2xvc19hdGVfZmltIiwiZ2VyZW5jaWFyX3Bhc3Rhc19ldGlxdWV0YXMiLCJhbHRlcmFyX2RhdGFfbGlzdGFfcHJvZHV0b3MiLCJnZXJlbmNpYXJfbW9kZWxvc19ldGlxdWV0YXMiLCJsaXN0YXJfdG9kb3NfdGlwb3NfYXJlYXNfYWNvZXMiLCJlZGl0YXJfY2FtcG9zX2FkaWNpb25haXNfY2FydGF6Il0sInNpZCI6IjE2NzgzODMyODMtYzdjNTE4YTktMDJkMi00ZmU0LWEyMjAtMWJlYzNkODAyMjZiIiwianRpIjoiMTY3ODM4MzI4My0yODI4ZDU1OS05M2I4LTQyN2EtYWYxZC1mN2MzMTY3ODQyOTMiLCJhdWQiOiJzbWFya2V0X3NvbHV0aW9ucyIsImlzcyI6InNtYXJrZXRfc29sdXRpb25zIiwiZXhwIjoxNjc4NDY5NjgzfQ.Vj8ApuZB0NWRPnGpPBWkH-CCRNs5z7TmfuZ-ae6emhUkBYgDfdBwt0OOZqEVKIbfG46nnaL6_UeR0LYnXeopeybe9jBmgbERbUDJxZE0hpfA--dF4IUF0qlpfYVd0NjMok4dugQFuNTJn9vwU6KQvyznoC6Of8zEwZEH5t5YOZVwlWAv4qZhTQCiOK1aTLvbJJXBp-wXHv2NXCy0zqXberTUDmSaqPQecvmT-xpdiIRi2IFmdlZZif_Drb6V1ACsZLyGDxvPTxmHs5nKBrfLy73lZ1MYK8K-lpvFOgIP9mle4jBY2gcve_xQcfY3jlZx6pMifhF9zn3Bl6MDsokSnQ'}
        debug()
        return True
    else:
        HEADERS = {"Authorization": f"Bearer {token}"}


def headers():
    global HEADERS
    global EXP_TIME

    if EXP_TIME is None or HEADERS is None:
        token, EXP_TIME = AuthRepositoryAPI().get_token()
        HEADERS = {"Authorization": f"Bearer {token}"}
        return HEADERS
    else:
        if datetime.datetime.now() > EXP_TIME:
            token, EXP_TIME = AuthRepositoryAPI().get_token()
            HEADERS = {"Authorization": f"Bearer {token}"}
            return HEADERS
        else:
            return HEADERS


def debug():
    global HEADERS

    HEADERS = {"x-smarket-user": 'teste', 'x-smarket-client-id': "onboarding", "x-smarket-user-id": "teste"}
    return True


def cliente() -> Client:
    return ClientService(ClientRepositoryAPI(headers())).get_client()


def database() -> Database:
    database = DatabaseService(DatabaseRepositoryAPI(headers())).get_database()
    return database


def oracle() -> Oracle:
    oracle = DatabaseService(DatabaseRepositoryAPI(headers())).get_oracle(database().database_id)
    return oracle


def segmento() -> Segment:
    return SegmentService(SegmentRepositoryAPI(headers())).get_segments()


def ping(message: str = 'PING', alive: bool = True, code: int = 99) -> bool:
    return PingerService(PingerRepositoryAPI(headers())).ping(message=message, alive=alive, code=code)


def phase2() -> Phase2:
    return Phase2Service(Phase2RepositoryAPI(headers())).get_phase2()


def sqls() -> SQLs:
    return SQLsService(SQLsRepositoryAPI(headers())).get_sqls()


def schedule() -> list[Schedule]:
    return ScheduleService(ScheduleRepositoryAPI(headers())).get_schedule()


def update_schedule(schedule_) -> bool:
    return ScheduleService(ScheduleRepositoryAPI(headers())).update_schedule(schedule_)


if __name__  == '__main__':
    #authenticate("eyJhbGciOiJSUzI1NiIsImtpZCI6IjE2NjcyNDg1MTAtMTZiNzljZTQtNDM1YS00YzA2LTkxZDItZjBjNjk5MzEyNjNkIiwidHlwIjoiSldUIn0.eyJzdWIiOiIxNTkiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJkYXZpX3NtYXJrZXQiLCJlbWFpbCI6ImRhdmlAc21hcmtldHNvbHV0aW9ucy5jb20uYnIiLCJjbGllbnRfaWQiOiJvbmJvYXJkaW5nIiwic3RvcmVzIjpbIjEiLCIxMCIsIjIiLCIyMDEiLCIyMDMiLCIyMiIsIjMiLCIzMDEiLCI0IiwiNSIsIjYiLCI3IiwiOCIsIjkiLCI5MDEiXSwicm9sZXMiOlsiYXByb3ZhY2FvIiwicmVsYXRvcmlvcyIsImRpYWdyYW1hZG9yIiwiZWRpdGFyX21hcGFzIiwibGlzdGFyX2Fjb2VzIiwibGlzdGFyX21hcGFzIiwiY29uZmlndXJhY29lcyIsImVkaXRhcl9jYXJ0YXoiLCJjYW5jZWxhcl9vZmVydGEiLCJkdXBsaWNhcl9vZmVydGEiLCJnZXJlbmNpYXJfYWNvZXMiLCJnZXJlbmNpYXJfYXJlYXMiLCJiYW5jb19kZV9pbWFnZW5zIiwiY3JpYXJfYXRpdmlkYWRlcyIsImVkaXRhcl9kZXNjcmljYW8iLCJnZXJlbmNpYXJfdG9rZW5zIiwibGlzdGFyX2NhbXBhbmhhcyIsInZlcl9sb2dzX29mZXJ0YXMiLCJnZXJlbmNpYXJfb2ZlcnRhcyIsInBlcmZpbF9wZXJtaXNzb2VzIiwiYXVkaXRhcl9hdGl2aWRhZGVzIiwiY3JpYXJfZWRpdGFyX2NpY2xvIiwiZWRpdGFyX3RleHRvX2xlZ2FsIiwiZ2VyZW5jaWFyX2NhcnRhemVzIiwiZ2VyZW5jaWFyX3VzdWFyaW9zIiwiZ2VyZW5jaWFyX2NhbXBhbmhhcyIsImdlcmVuY2lhcl9jb250cmF0b3MiLCJnZXJlbmNpYXJfZXRpcXVldGFzIiwiYWx0ZXJhcl9wcm9kdXRvX2FjYW8iLCJhbHRlcmFyX3Jlc3BvbnNhdmVpcyIsImdlcmVuY2lhcl90aXBvX2RlX2FyZWEiLCJlZGl0YXJfZGVzY3JpY2FvX2NhcnRheiIsImdlcmVuY2lhcl9wYXN0YXNfY2FydGF6Iiwic21hcmtldGZ5X2F0aXZvX3VzdWFyaW8iLCJhcHJvdmFyX29mZXJ0YXNfaW50ZXJuYXMiLCJ2aXN1YWxpemFyX2NpY2xvc19hdGVfZmltIiwiZ2VyZW5jaWFyX3Bhc3Rhc19ldGlxdWV0YXMiLCJhbHRlcmFyX2RhdGFfbGlzdGFfcHJvZHV0b3MiLCJnZXJlbmNpYXJfbW9kZWxvc19ldGlxdWV0YXMiLCJsaXN0YXJfdG9kb3NfdGlwb3NfYXJlYXNfYWNvZXMiLCJlZGl0YXJfY2FtcG9zX2FkaWNpb25haXNfY2FydGF6Il0sInNpZCI6IjE2ODA2OTk1MTktNGZlYmE5NGEtZjRmMS00ODRlLTlmYjMtZWQ0MDNiZmRlMzQ3IiwianRpIjoiMTY4MDY5OTUxOS0wNTk5ZjVmMS1iOTRmLTQ0ZDUtYmY0ZC01YTQ5YWRiYTEyOGEiLCJhdWQiOiJzbWFya2V0X3NvbHV0aW9ucyIsImlzcyI6InNtYXJrZXRfc29sdXRpb25zIiwiZXhwIjoxNjgwNzg1OTE5fQ.NMTrLc_J5rFvBQj4wmaQ2mzMPRt4iFojDDByfdD36eznphbWPamDLZzhTcN6xOcNngaB-qDWrKXq4q8JIQrQ1B66SveJOPgGcLPYOz03iorQ_zJRdWbCmFvJ3pw5d288gVnHwAT02jGnNBqaXxuKaFXRYJn5AIh8Oy7x-vM6R_U5mDo9DKdIspmDARziLSaULuETGnEwSG7qdOesW1rAuRPIwFDFC-QLpbYJ7dQekvqZsvIFIxZEAd8qWmoVmZlfqSi6s4XDzios1J5mom8r8v9MN4TPuLhUakfAxsvfCfY7NxuJKJHZ-kEZ70en49-drnQjhBHAIFehPJokKphgyw")
    print(cliente().client_id)
    print()
    headers()