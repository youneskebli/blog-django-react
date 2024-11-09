import { createBrowserRouter } from "react-router-dom";
import Home from "./pages/dashboard";
import ErrorPage from "./pages/404";
import Articles from "./pages/articles";
import Layout from "./components/layout";
import Dashboard from "./pages/dashboard";
import AddArticle from "./pages/add-article";
import ArticlePage from "./pages/article";

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
        path: "/add-article",
        element: <AddArticle />,
      },
    ],
  },
]);

export default router;
