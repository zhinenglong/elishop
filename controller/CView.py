import typing as t
from . import ft, views, current_app, request

class CView(views.View):

    @classmethod
    def to_view(
        cls, name: str, handle_name: str, *class_args: t.Any, **class_kwargs: t.Any
    ) -> ft.RouteCallable:
        if cls.init_every_request:
            def view(**kwargs: t.Any) -> ft.ResponseReturnValue:
                self = view.view_class(  # type: ignore[attr-defined]
                    *class_args, **class_kwargs
                )
                handle = getattr(self,handle_name, None)
                if handle is not None:
                    return current_app.ensure_sync(handle)(**kwargs)
                return current_app.ensure_sync(self.dispatch_request)(**kwargs)

        else:
            self = cls(*class_args, **class_kwargs)

            def view(**kwargs: t.Any) -> ft.ResponseReturnValue:
                handle = getattr(self, handle_name, None)
                if handle is not None:
                    return current_app.ensure_sync(self.handle)(**kwargs)
                return current_app.ensure_sync(self.dispatch_request)(**kwargs)

        if cls.decorators:
            view.__name__ = name
            view.__module__ = cls.__module__
            for decorator in cls.decorators:
                view = decorator(view)


        view.view_class = cls  # type: ignore
        view.__name__ = name
        view.__doc__ = cls.__doc__
        view.__module__ = cls.__module__
        view.methods = cls.methods  # type: ignore
        view.provide_automatic_options = cls.provide_automatic_options  # type: ignore
        return view