import { createBrowserRouter } from "react-router-dom";
import ErrorPage from "./pages/404";
import Articles from "./pages/articles";
import Layout from "./components/layout";
import Dashboard from "./pages/dashboard";
import AddArticle from "./pages/add-article";
import ArticlePage from "./pages/article";
import Login from "./pages/login.tsx";
import EditedArticles from "./pages/edited-articles.tsx";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    errorElement: <ErrorPage />,
    children: [
      {
        path: "",
        element: <Dashboard />,
      },
      {
        path: "/articles/:id",
        element: <ArticlePage />,
      },
      {
        path: "/articles",
        element: <Articles />,
      },
      {
        path: "/articles-edited",
        element: <EditedArticles />,
      },
      {
        path: "/add-article",
        element: <AddArticle />,
      },
    ],
  },
    {
    path: "/login",
    element: <Login />,
  },
]);


export default router;
