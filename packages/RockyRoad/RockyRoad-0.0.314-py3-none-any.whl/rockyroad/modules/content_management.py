from .module_imports import *


@headers({"Ocp-Apim-Subscription-Key": key})
class Content_Management(Consumer):
    """Inteface to Cms_Page resource for the RockyRoad API."""

    def __init__(self, Resource, *args, **kw):
        self._base_url = Resource._base_url
        super().__init__(base_url=Resource._base_url, *args, **kw)

    def cms_page(self):
        return self.Cms_Page(self)

    @headers({"Ocp-Apim-Subscription-Key": key})
    class Cms_Page(Consumer):
        """Inteface to Cms_Page resource for the RockyRoad API."""

        def __init__(self, Resource, *args, **kw):
            self._base_url = Resource._base_url
            super().__init__(base_url=Resource._base_url, *args, **kw)

        def cms_page_field(self):
            return self.Cms_Page_Field(self)

        @returns.json
        @http_get("content-management/pages")
        def list(self, param: Query(type=str) = None):
            """This call will return list of Cms_Page_Objects."""

        @http_get("content-management/pages/{uid}")
        def get(self, uid: str):
            """This call will get the Cms_Page_Object for the specified uid."""

        @delete("content-management/pages/{uid}")
        def delete(self, uid: str):
            """This call will delete the Cms_Page_Object for the specified uid."""

        @returns.json
        @json
        @post("content-management/pages")
        def insert(self, cms_page_object: Body):
            """This call will create the Cms_Page_Object with the specified parameters."""

        @json
        @patch("content-management/pages/{uid}")
        def update(self, uid: str, cms_page_object: Body):
            """This call will update the Cms_Page_Object with the specified parameters."""

        @headers({"Ocp-Apim-Subscription-Key": key})
        class Cms_Page_Field(Consumer):
            """Inteface to Cms_Page_Field resource for the RockyRoad API."""

            def __init__(self, Resource, *args, **kw):
                self._base_url = Resource._base_url
                super().__init__(base_url=Resource._base_url, *args, **kw)

            @returns.json
            @http_get("content-management/pages/fields")
            def list(
                self,
                param: Query(type=str) = None,
            ):
                """This call will return list of Cms_Page_Fields."""

            @returns.json
            @http_get("content-management/pages/fields/{uid}")
            def get(self, uid: str):
                """This call will return list of Cms_Page_Fields."""

            @delete("content-management/pages/fields/{uid}")
            def delete(self, uid: str):
                """This call will the Cms_Page_Field."""

            @returns.json
            @json
            @post("content-management/pages/{cms_page_uid}/fields")
            def insert(self, cms_page_uid: str, cms_page_field_object: Body):
                """This call will create the Cms_Page_Field."""

            @json
            @patch("content-management/pages/fields/{uid}")
            def update(self, uid: str, cms_page_field_object: Body):
                """This call will update the Cms_Page_Field."""
