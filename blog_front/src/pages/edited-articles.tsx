import { useQuery } from "@tanstack/react-query";
import ArticlesTable from "../components/articles-table";
import Article from "../domain/article";
import { getEditedArticles } from "../api/article";
import { Link } from "react-router-dom";

const EditedArticles = () => {
  const {
    data: articles,
    error,
    isError,
    isLoading,
  } = useQuery<Article[], Error>({
    queryKey: ["edited-articles"],
    queryFn: getEditedArticles,
  });

  // if (isLoading) return "Loading ...";
  // if (isError) return <p className="text-error">{error?.message}</p>;
  return (
    <>
      <div className="breadcrumbs text-sm mb-10">
        <ul>
          <li>
            <Link to={"/"}>Dashboard</Link>
          </li>
          <li>Edited Articles</li>
        </ul>
      </div>

      <h1 className="text-3xl font-bold mb-10">Articles</h1>
      <ArticlesTable articles={articles || []} />
    </>
  );
};

export default EditedArticles;
