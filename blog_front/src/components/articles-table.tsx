import { useNavigate } from "react-router-dom";
import Article, { Status } from "../domain/article";
import TableHeader from "./table-header";
import { useMutation } from "@tanstack/react-query";
import { patchArticle } from "../api/article";
import { queryClient } from "../main";

const fields = ["#", "title", "status"];

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
  const { mutate, isPending } = useMutation({
    mutationFn: (status: Status) => patchArticle({
      ...article,
      status
    }),
    onSuccess: () => {
      queryClient.invalidateQueries();
    },
    onError: (error: any) => {
      console.error("Error adding article post:", error);
    },
  });

  return (
    <tr>
      <td>{article.id}</td>
      <td onClick={() => navigate(`${article.id}`)}
      className="hover:bg-slate-300 cursor-pointer">{article.title}</td>
      <td className="flex items-center gap-2"> {article.status} 
      {
        article.status == "PENDING" &&
        <>
          <button disabled={isPending} onClick={()=>mutate("REJECTED")} className="btn btn-square bg-error ml-40">x</button>
          <button disabled={isPending} onClick={()=>mutate("APPROVED")} className="btn btn-square bg-[#46b664]">+</button>
        </>
      }
      </td>
    </tr>
  );
};

export default ArticlesTable;
