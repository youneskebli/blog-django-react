import { Link } from "react-router-dom";
import AddArticleForm from "../components/add-article-form";

const AddArticle = () => {
  return (
    <>
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
      <h1 className="text-3xl font-bold mb-10">Add article</h1>
      <AddArticleForm />
    </>
  );
};

export default AddArticle;
