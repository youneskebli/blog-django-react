import Writer from "../domain/writer";
import TableHeader from "./table-header";

const fields = ["name", "Articles Written", "Total Articles In 30"];

const WritersTable = ({ writers }: { writers: Writer[] }) => {
  return (
    <div className="overflow-x-auto">
      <table className="table">
        <TableHeader fields={fields} />
        <tbody>
          {writers.map((b) => (
            <TableRow key={b.id} writer={b} />
          ))}
        </tbody>
      </table>
    </div>
  );
};

const TableRow = ({ writer }: { writer: Omit<Writer, "id"> }) => {
  return (
    <tr>
      <td>{writer.name}</td>
      <td>{writer.total_articles}</td>
      <td>{writer.articles_last_30_days}</td>
    </tr>
  );
};

export default WritersTable;
