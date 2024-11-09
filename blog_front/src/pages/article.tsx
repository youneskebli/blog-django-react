import { useQuery } from "@tanstack/react-query";
import Article from "../domain/article";
import { getArticleById } from "../api/article";
import { Link, useParams } from "react-router-dom";
import EditArticle from "../components/edit-article";

const ArticlePage = () => {
  const { id } = useParams();
  const {
    data: article,
    error,
    isError,
    isLoading,
  } = useQuery<Article, Error>({
    queryKey: ["article"],
    queryFn: () => getArticleById(parseInt(id || "")),
  });

  if (!article) return <p>Not Found</p>
  return (
    <article>
      <div className="breadcrumbs text-sm mb-10 ml-5">
        <ul>
          <li>
            <Link to={"/"}>Dashboard</Link>
          </li>
          <li>
            <Link to={"/articles"}>Articles</Link>
          </li>
          <li>Edit Article</li>
        </ul>
      </div>
      <EditArticle article={article} />
    </article>
  );
};

export default ArticlePage;
