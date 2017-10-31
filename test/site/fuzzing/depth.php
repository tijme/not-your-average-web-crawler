<!DOCTYPE html>
<html>
    <body>
        <?php
            $depth = 15000 - 1;
            $current = isset($_GET['depth']) ? (int) $_GET['depth'] : 1;

            $from = $current <= $depth && $current >= 1 ? $current : 1;
            $to = $from + 100 <= $depth && $from >= 1 ? $from + 100 : $depth;

            for ($i = $from; $i <= $to; $i ++) {
                echo '<a href="?depth=' . $i . '">Depth: ' . $i . '</a><br>';
            }
        ?>
    </body>
</html>