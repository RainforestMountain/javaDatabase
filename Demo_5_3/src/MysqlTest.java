import com.mysql.cj.jdbc.MysqlDataSource;

import javax.sql.DataSource;
import java.sql.*;

public class MysqlTest {
    public static void main(String[] args) throws SQLException {
        DataSource ds = new MysqlDataSource();
        ((MysqlDataSource) ds).setURL("jdbc:mysql://127.0.0.1:3306/business?characterEncoding=UTF-8&useSSL=false");
        ((MysqlDataSource) ds).setUser("root");
        ((MysqlDataSource) ds).setPassword("123456");
        Connection connection = ds.getConnection();
        String sql = "select * from business_table;";
        PreparedStatement preparedStatement = connection.prepareStatement(sql);
        ResultSet resultSet = preparedStatement.executeQuery();

        while (resultSet.next()) {
            for (int i = 0; i < 10; i++) {
                try {
                    String str = resultSet.getString(i);
                    System.out.print(str + " ");
                } catch (Exception e) {

                }
            }
            System.out.println();
        }

        resultSet.close();
        preparedStatement.close();
        connection.close();

    }
}
