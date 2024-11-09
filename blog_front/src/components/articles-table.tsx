import { useNavigate } from "react-router-dom";
import Article from "../domain/article";
import TableHeader from "./table-header";

const fields = ["#", "title"];

const ArticlesTable = ({ articles }: { articles: Article[] }) => {
  return (
    <div className="overflow-x-auto">
      <table className="table">
        <TableHeader fields={fields} />
        <tbody>
          {articles.map((b) => (
            <ArticlesTableRow key={b.id} article={b} />
          ))}
        </tbody>
      </table>
    </div>
  );
};

const ArticlesTableRow = ({ article }: { article: Article }) => {
  const navigate = useNavigate();
  return (
    <tr
      onClick={() => navigate(`${article.id}`)}
      className="hover:bg-slate-300 cursor-pointer">
      <td>{article.id}</td>
      <td>{article.title}</td>
    </tr>
  );
};

export default ArticlesTable;
