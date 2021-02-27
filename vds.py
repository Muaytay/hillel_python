class BaseClient:
    def get(
        self,
        url: str,
        params: Optional[dict] = None,
        headers: Optional[dict] = None,
        **kwargs,
    ) -> Response:
        resp = requests.get(url=url, params=params, headers=headers, **kwargs)
        if resp.status_code != 200:
            if resp.status_code >= 500 or resp.status_code == 404:
                raise HTTPException(resp.status_code, resp.text)
            raise HTTPException(resp.status_code, resp.json())

        return resp

    class BaseClient:
        def get(
                self,
                url: str,
                params: Optional[dict] = None,
                headers: Optional[dict] = None,
                **kwargs,
        ) -> Response:
            resp = requests.get(url=url, params=params, headers=headers, **kwargs)
            if resp.status_code != 200:
                if resp.status_code >= 500 or resp.status_code == 404:
                    raise HTTPException(resp.status_code, resp.text)
                raise HTTPException(resp.status_code, resp.json())

            return resp

        def post(
                self,
                url: str,
                data: Optional[dict] = None,
                json: Optional[dict] = None,
                headers: Optional[dict] = None,
                **kwargs
        ) -> Response:
            resp = requests.post(url=url, data=data, json=body, headers=headers, **kwargs)
            if resp.status_code not in (200, 201):
                if resp.status_code >= 500:
                    raise HTTPException(resp.status_code, resp.text)
                raise HTTPException(resp.status_code, resp.json())

            return resp

